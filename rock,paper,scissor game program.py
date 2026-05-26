# rock paper scissor game
import random
choices = ["rock","paper","scissors"]
computer = random.choice(choices)
user = input("Enter rock,paper or scissors:").lower()
print("computer chose:",computer)
if user == computer:
    print("Tie")
elif ((user == "rock" and computer == "scissors") or
     (user =="scissors" and computer == "paper")or
     (user == "paper" and computer == "rock")):
         print("you win")
else:
    print("computer wins")
         
