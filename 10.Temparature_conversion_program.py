#Temparature conversion program

unit=input("F or C: ")
temp=float(input("enter temp: "))

if unit=="C":
    temp=round((9*temp)/5+32,1)
    print(f"the temparature in Fahreneit is {temp}")
elif unit=="F":
    temp=round((temp-32)*5/9,1)
    print(f"the temparature in Celcius is {temp}")
else:
    print(f"{unit} is unvalid")
