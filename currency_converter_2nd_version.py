#ASKS FOR TL TO CONVERT TO OTHER CURRENCİES

import requests
import json

# --- API Keys and Endpoints ---
# Your Gold API key
GOLD_API_KEY = "goldapi-913wsmgc7owyw-io"

# Fiat URL (Frankfurter API): Base is EUR, fetching USD and TRY for calculation
FIAT_URL = "https://api.frankfurter.app/latest?symbols=USD,TRY"

# Crypto URL (CoinGecko API): BTC, ETH prices in USD and TRY
CRYPTO_URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd,try"

# Dedicated Gold API endpoint (XAU/USD)
GOLD_USD_URL = "https://www.goldapi.io/api/XAU/USD"


def get_user_amount():
    """Prompts the user for a valid numerical input."""
    while True:
        try:
            # Ask the user how much Turkish Lira (TL) they have
            amount_str = input("\nEnter the amount in Turkish Lira (TL) you want to convert: ")
            amount = float(amount_str)
            if amount < 0:
                print("Amount must be a positive number. Try again.")
                continue
            return amount
        except ValueError:
            print("Invalid input. Please enter a numerical value.")


def get_and_display_rates():
    """Fetches, calculates, and displays all current exchange rates based on user input."""

    # --- 0. Setup Gold Request Headers ---
    gold_headers = {
        "x-access-token": GOLD_API_KEY,
        "Content-Type": "application/json"
    }

    # Initialize variables outside of try blocks
    usd_try_rate = 0.0
    gold_usd_ounce = 0.0
    crypto_data = {}

    # --- 1. Fetch Fiat Rates (USD/TRY) via Frankfurter ---
    try:
        fiat_response = requests.get(FIAT_URL)
        fiat_response.raise_for_status()
        fiat_data = fiat_response.json()

        # Calculate USD/TRY cross-rate from EUR base
        eur_usd_rate = fiat_data['rates']['USD']
        eur_try_rate = fiat_data['rates']['TRY']
        usd_try_rate = eur_try_rate / eur_usd_rate

        print(f"Base USD/TRY Exchange Rate: 1 USD = {usd_try_rate:.4f} TL")

    except requests.exceptions.RequestException as e:
        print(f"FATAL ERROR: Failed to connect to the Frankfurter API. Cannot proceed. Error: {e}")
        return

        # --- 2. Fetch Crypto Prices (BTC/ETH) ---
    try:
        crypto_response = requests.get(CRYPTO_URL)
        crypto_response.raise_for_status()
        crypto_data = crypto_response.json()

    except requests.exceptions.RequestException as e:
        print(f"WARNING: Failed to connect to the Crypto API. Crypto prices may be missing. Error: {e}")

    # --- 3. Fetch Gold Price (GoldAPI.io) ---
    try:
        # 🟢 Pass the gold_headers with the API key
        gold_response = requests.get(GOLD_USD_URL, headers=gold_headers)
        gold_response.raise_for_status()

        gold_data = gold_response.json()
        gold_usd_ounce = float(gold_data['price'])

    except requests.exceptions.HTTPError as e:
        print(f"WARNING: Gold API request failed! Check your key or usage limit. HTTP Error: {e.response.status_code}")
    except (requests.exceptions.RequestException, KeyError) as e:
        print(f"WARNING: Could not fetch or parse Gold price data. Error: {e}")

    # --- 4. Get User Input and Calculate Conversions ---

    # Get the amount the user wants to convert (e.g., how much TL)
    input_amount_try = get_user_amount()

    # Calculate the equivalent USD amount for the input TRY
    input_amount_usd = input_amount_try / usd_try_rate

    print(f"\n--- CONVERSION RESULTS for {input_amount_try:,.2f} TL ({input_amount_usd:,.2f} USD) ---")
    print("-" * 50)

    # --- Bitcoin (BTC) DISPLAY ---
    btc_try = crypto_data.get('bitcoin', {}).get('try', None)
    if btc_try is not None:
        # Calculation: Input TRY amount / Price of 1 BTC in TRY
        btc_amount = input_amount_try / btc_try
        print(f"Bitcoin (BTC): {btc_amount:.6f} BTC")
    else:
        print("Bitcoin (BTC): Data Not Available")

    # --- ETH DISPLAY ---
    eth_try = crypto_data.get('ethereum', {}).get('try', None)
    if eth_try is not None:
        # Calculation: Input TRY amount / Price of 1 ETH in TRY
        eth_amount = input_amount_try / eth_try
        print(f"Ethereum (ETH): {eth_amount:.6f} ETH")
    else:
        print("Ethereum (ETH): Data Not Available")

    print("-" * 50)

    # --- GOLD DISPLAY ---
    if gold_usd_ounce > 0 and usd_try_rate > 0:
        # Calculate the price of 1 Ounce of Gold in TRY
        gold_try_ounce_rate = gold_usd_ounce * usd_try_rate

        # Calculation: Input TRY amount / Price of 1 Ounce of Gold in TRY
        xau_amount = input_amount_try / gold_try_ounce_rate
        print(f"Gold (XAU Ounce): {xau_amount:.6f} XAU Ounce")
    else:
        print("Gold (XAU Ounce): Data Not Available")

    print("-" * 50)


if __name__ == "__main__":
    get_and_display_rates()