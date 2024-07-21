import random
print("Welcome to the game of luck.")

List12 = [1,2,1,1,3,4,4]
x = random.choice(List12)


a = input("Input your guess: ")

if int(a) == int(x):
    print("You won the game")
else:
    print("Try again")

    

