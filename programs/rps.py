'''
TITLE: rps.py
Description: Rock Paper Scissors game vs computer.
Author: Shiwansh Bind
Requirements: Python 3.0+
'''

import random

print("=== Rock Paper Scissors ===")

# list of all valid choices
choices = ["rock", "paper", "scissors"]

# simple score counters
wins = 0
losses = 0
draws = 0

while True:
    you = input("Enter rock/paper/scissors (or quit): ").lower().strip()

    if you == "quit":
        break

    if you not in choices:
        print("Invalid! Type rock, paper or scissors.")
        continue

    computer = random.choice(choices)
    print(f"Computer chose: {computer}")

    if you == computer:
        print("Draw!")
        draws = draws + 1
    elif you == "rock" and computer == "scissors":
        print("You win! Rock beats scissors.")
        wins = wins + 1
    elif you == "paper" and computer == "rock":
        print("You win! Paper beats rock.")
        wins = wins + 1
    elif you == "scissors" and computer == "paper":
        print("You win! Scissors beats paper.")
        wins = wins + 1
    else:
        print("You lose!")
        losses = losses + 1

    print(f"Score -> Wins: {wins}, Losses: {losses}, Draws: {draws}")
    print()

print(f"Final -> Wins: {wins}, Losses: {losses}, Draws: {draws}")
print("Thanks for playing!")
