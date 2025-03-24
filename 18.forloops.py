# for loops=execute a block of code a fixed number of times
#     You can iterate over a range,string sequence, etc.

#ranges second number(11) is exclussive so if we want to make 10 write 11

#for x in range(1,11):
 #   print(x)

#for x in reversed(range(1, 11)):    reverse version
 #   print(x)
#print("HAPPY NEW YEAR")

#for x in range(1,11,2):
 #   print(x)    #1,3,5,7,9

 # You can iterate through a string with for loop

credit_number= "1234-5678-9012"
for x in credit_number:   #1234-5678
    print(x)

for x in range(1,21):
    if x==13:
        continue
    else:
        print(x)  #13 hariç hepsini printliyor