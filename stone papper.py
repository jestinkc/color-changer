import random

choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
player = input("Enter rock, paper, or scissors: ")
print(f"Computer chose {computer}. You lose!")

