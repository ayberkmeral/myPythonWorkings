# we have used tuple because we wont change
#BIDAHA IZLE ANLAMADIM
import random

options=("rock","paper","scissors")
player =None
computer=random.choice(options)

running=True

while running:

    player = None
    computer = random.choice(options)
    while player  not in options:
       player=input("enter a choice (rock paper scissors): ")

    print(f"Player:{player}")
    print(f"Computer:{computer}")

    if player==computer:
        print("its tie")
    elif player =="rock" and computer=="scissors":
        print("u win")
    elif player =="paper" and computer=="rock":
        print("u win")
    elif player =="scissors" and computer=="paper":
        print("u win")
    else:
        print("u lose")
    if not input("play again: ").lower()=="y":
        running=False
