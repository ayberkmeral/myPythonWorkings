#JUST CONVERTS 1 CURRENY TO ANOTHER

import requests

import json

GOLD_API_KEY="goldapi-913wsmgc7owyw-io"  #It allows the API provider to enforce a rate limit (e.g., "you can only make 100 calls per day on the free plan").

FIAT_URL="https://api.frankfurter.app/latest?symbols=USD,TRY" #api end point

CRYPTO_URL="https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,gold&vs_currencies=usd,try"

GOLD_USD_URL="https://www.goldapi.io/api/XAU/USD"

def get_and_display_rates():
    gold_headers = {   #This step was necessary for the Gold API but not for the Crypto or Fiat APIs because of the difference in their security models and data availability.
        "x-access-token": GOLD_API_KEY,
        "Content-Type": "application/json"
    }

    #gold_usd_ounce = 0.0
    #USD RATES
    try:
        fiat_response=requests.get(FIAT_URL)
        fiat_response.raise_for_status() #If the response indicates an error (status codes 4xx or 5xx), it will raise an exception (HTTPError).
        fiat_data=fiat_response.json()


        eur_usd_rate=fiat_data['rates']['USD'] #These two lines are extracting specific currency values from the API response dictionary (fiat_data).
        eur_try_rate=fiat_data['rates']['TRY']

        usd_try_rate= eur_try_rate/eur_usd_rate

        print(f"Current USD/TRY Exchange Rate:1 USD={usd_try_rate} TL/n")

    except requests.exceptions.RequestException as e:
        print(f"FATAL ERROR: Failed to connect to the Frankfurter API. Error: {e}")
        return  # Stop execution if the essential API fails


    #CRYPTO RATES
    try:
        crypto_response=requests.get(CRYPTO_URL)
        crypto_response.raise_for_status()
        crypto_data=crypto_response.json()

    except requests.exceptions.RequestException as e:
        print(f"FATAL ERROR: Failed to connect to the Crypto/Gold API. Error: {e}")
        return

    print("CURRENT CROSS-RATE TABLE")

    #GOLD RATES
    try:
        gold_response=requests.get(GOLD_USD_URL, headers=gold_headers)
        gold_response.raise_for_status()
        gold_data=gold_response.json()
        gold_usd_ounce=float(gold_data['price'])
    except requests.exceptions.HTTPError as e: #(The Child): This is a more specific exception that is raised only when the server is successfully reached, but it sends back a "bad" response status code (4xx or 5xx). This error is created when you call the method .401 Unauthorized:
        print(f"WARNING: Gold API request failed! Check your key or usage limit. HTTP Error: {e.response.status_code}")
    except (requests.exceptions.RequestException, KeyError) as e:  # (The Parent): This is the catch-all exception for fundamental problems with the request itself. It catches errors that happen before the server returns a valid response, such as:No internet connection .The server takes too long to respond.DNS issues.
        print(f"WARNING: Could not fetch or parse Gold price data. Error: {e}")


    # Bitcoin (BTC) DISPLAY
    btc_usd=crypto_data.get('bitcoin',{}).get('usd','N/A')  #.get('bitcoin', {}) → looks inside the dictionary for the "bitcoin" key. If "bitcoin" doesn’t exist, return an empty {} instead of crashing.
    btc_try=crypto_data.get('bitcoin',{}).get('try','N/A') #N/A → Not Available
    print(f"1 BTC={btc_try:.4f} TRY")
    print(f"1 BTC={btc_usd:.4f} USD")
    print("-"*30)

    #ETH DISPLAY
    eth_usd=crypto_data.get('ethereum',{}).get('usd','N/A')
    eth_try=crypto_data.get('ethereum',{}).get('try','N/A')
    print(f"1 ETH={eth_try:.4f} TRY")
    print(f"1 ETH={eth_usd:.4f} USD")
    print("-"*30)

    #GOLD DISPLAY

    if gold_usd_ounce>0:
        gold_try_ounce=gold_usd_ounce*usd_try_rate
        print(f"1 TROY OF OUNCE GOLD(XAU)={gold_try_ounce:.4f}TL")
        print(f"1 TROY OF OUNCE GOLD(XAU)={gold_usd_ounce:.4f}USD")
    else:
        print("1 TROY OF OUNCE GOLD(XAU) WAS NOT AVAİLABLE")

    print("-"*30)




if __name__=="__main__":
    get_and_display_rates()


