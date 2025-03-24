#Python compound interest calculator

principle=0
time=0
rate=0

while True:
    principle=float(input("enter the principle: "))
    if principle<0:
        print("principle cant be negative ")
    else:
        break

while True:
    rate=float(input("enter the rate: "))
    if rate<=0:
        print("rate cant be negative ")
    else:
        break

while True:
    time=int(input("enter the time in years: "))
    if time<=0:
        print("time cant be negative ")
    else:
        break


total=principle*pow((1+rate/100),time)
print(f"after {time} years your total is ${total:.2f}")