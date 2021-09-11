import random
chance = 0
a = 1
print("secret number game")
print("secret game is ,to guess number from the given range if you guess you win")
a = int(input("press 1 to start a game :"))

if a != 1:
    print("enter 1 to start game")
else:
    print("game starts")
    b = int(input("how many trials you want for playing the game:"))
while chance != b:
    # b = int(input("how many trials you want for playing the game:"))
    print("chance = ", chance + 1)
    guess = int(input("enter number between the range 10-100"))
    #guess = int(input(""))
    Num_guesses = random.randint(10, 101)
    if guess == Num_guesses:
        print("congratulations you win")
        break
    elif guess > 100:
        print("But you cheated!")
    elif guess > Num_guesses:
        print("please lower number")
    elif guess < Num_guesses:
        print("please higher number")
    chance += 1
print("game over")
print("number of chances you take",chance)