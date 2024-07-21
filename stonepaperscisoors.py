import random

LX = ["Rock", "Paper", "Scissors"]

x = random.choice(LX)
y = input("Type here(Stone/Paper/Scissors): ")
print(y)

if x == y:
    print("You win")
else:
    print("You lose")

