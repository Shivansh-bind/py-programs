'''
TITLE: quiz.py
Description: Simple GK quiz game with score.
Author: Shiwansh Bind
Requirements: Python 3.0+
'''

print("=== GK Quiz ===")
print("Type your answer and press Enter.")
print()

# score starts at 0
score = 0

ans1 = input("1. How many days in a week? ").strip().lower()
if ans1 == "7" or ans1 == "seven":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! Answer is 7.")

ans2 = input("2. What color is the sky on a clear day? ").strip().lower()
if ans2 == "blue":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! Answer is blue.")

ans3 = input("3. Which animal says meow? ").strip().lower()
if ans3 == "cat":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! Answer is cat.")

ans4 = input("4. 2 + 3 = ? ").strip().lower()
if ans4 == "5" or ans4 == "five":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! Answer is 5.")

ans5 = input("5. Capital of India? ").strip().lower()
if ans5 == "delhi" or ans5 == "new delhi":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! Answer is Delhi.")

print()
print(f"Your final score: {score} / 5")

if score == 5:
    print("Amazing! Full marks!")
elif score >= 3:
    print("Good job!")
else:
    print("Try again!")
