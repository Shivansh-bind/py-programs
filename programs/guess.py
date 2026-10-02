'''
TITLE: guess.py
Description: Number guessing game, similar fun to Wordle.
Author: Shiwansh Bind
Requirements: Python 3.0+
'''

# random lets the computer pick a secret number
import random

print("=== Guess The Number ===")
print("I picked a number from 1 to 20. Try to guess it!")

secret = random.randint(1, 20)

# history list remembers all tries
tries = []

while True:
    guess = int(input("Your guess: "))
    tries.append(guess)
    print("Your tries so far:", tries)

    if guess == secret:
        print(f"Correct! You did it in {len(tries)} tries.")
        break

    if guess < secret:
        print("Too low! Go higher.")
    else:
        print("Too high! Go lower.")

    # abs() tells how close we are
    diff = abs(secret - guess)
    if diff <= 2:
        print("Very hot! Almost there.")
    elif diff <= 5:
        print("Warm.")
    else:
        print("Cold.")
