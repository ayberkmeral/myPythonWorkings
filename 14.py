# while loop =executes some code while some condition remains true

name =input("enter ur name")

while name=="":
    print("u did not enter ur name")
    name = input("enter ur name")
else:
    print(f"ur name is {name}")


age=int(input("enter ur age"))

while age<0:
    print("age cant be negative")
    age = int(input("enter ur age"))
else:
    print(f"ur age is {age}")


food=input("enter food u like enter q to quit")

while not food == "q":
    print(f"ur food is {food}")
    food = input("enter food u like enter q to quit")

print("bye")


num=int(input("enter between 1-10"))

while num<1 or num>10:
    print(f"{num} not valid")
    num=int(input("enter between 1-10"))

print("bye")
