'''
TITLE: dice.py
Description: Dice roller game, roll 2 dice and check doubles.
Author: Shiwansh Bind
Requirements: Python 3.0+
'''

import random

print("=== Dice Roller ===")
print("Roll 2 dice. Same number = doubles, you win!")

rolls = 0

while True:
    choice = input("Press Enter to roll (or type quit): ").strip().lower()

    if choice == "quit":
        break

    # randint(1, 6) picks 1 to 6 like a real dice
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    total = d1 + d2
    rolls = rolls + 1

    print(f"Dice: {d1} + {d2} = {total}")

    if d1 == d2:
        print("Doubles! You win!")
    elif total == 7 or total == 11:
        print("Lucky 7 / 11!")
    else:
        print("No win, roll again.")

    print(f"Total rolls: {rolls}")
    print()

print(f"You rolled {rolls} times. Bye!")
