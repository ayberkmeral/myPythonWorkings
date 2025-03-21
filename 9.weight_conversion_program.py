#Python weight converter

weight=float(input("enter your weight: "))
unit=input("enter K or L: ")

if unit.upper()=="K":
    weight=weight*2.205
    unit="Lbs."
    print(f"u are {round(weight, 1)} {unit}")
elif unit.upper()=="L":
    weight=weight/2.205
    unit="Kg"
    print(f"u are {round(weight, 1)} {unit}")
else:
    print(f"{unit} was not valid")

