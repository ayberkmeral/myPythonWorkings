#nested loops =A loop within another loop(outer,inner)
#     outer loop
#       inner loop





for x in range(3):
    for x in range(1, 10):
        print(x, end="")
    print()


rows=int(input("enter row number"))
columns=int(input("enter column number"))
symbol=input("enter symbol")

for x in range(rows):
    for x in range(1,columns):
        print(symbol, end="")
    print()