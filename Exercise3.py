from random import randint
number=randint(0,100)
guess = int(input("Make a guess: "))
while guess != number:
    if number < guess:
        guess=int(input("Decrease your number: "))
    else:
        guess=int(input("Increase your number: "))
print("You got it right!")



