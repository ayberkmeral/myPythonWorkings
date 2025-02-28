import time #this is a pyhton module

#time.sleep(3) #the program will sleep for three seconds

my_time=int(input("enter your time in seconds"))

#for x in range(my_time,0,-1):

#    print(x)
#    time.sleep(1)

#print("Time's Up")

#for x in reversed(range(0,my_time)):
#    print(x)                                 aynı mantık
#    time.sleep(1)

#print("Time's Up")

for x in range(my_time,0,-1):
    seconds=x%60
    minutes = int(x/60)%60   #mod 60 ı anlamadım
    print(f"00:00:{seconds:02}")  #02 makes padding I did not understand
    time.sleep(1)


    #-----WATCH FROM THE BEGINNING-----