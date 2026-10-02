'''
TITLE: Wordle.py
Description: A simple word guessing game where the user has to guess a 5-character word in 5 tries.
Author: Shiwansh Bind
Github: [github.com/shivansh-bind](http://github.com/shivansh-bind)
Requirements: Tested on Python 3.14.7+ ; might work on older versions 3.0+
Version: 0.0.12
'''

# library used for randomly selecting a word from the list of words
import random

#   only 5 character words
#   Categorised based on english word frequency
easy_words = [
    "apple", "house", "water", "plant", "table",
    "chair", "world", "earth", "happy", "green",
    "light", "bread", "stone", "phone", "music",
    "river", "cloud", "heart", "smile", "beach"
]

medium_words = [
    "flame", "grape", "ocean", "dream", "brush",
    "storm", "train", "crown", "proud", "sharp",
    "quiet", "fresh", "brave", "sweep", "crane",
    "spear", "frost", "wheat", "track", "plain"
]

expert_words = [
    "quilt", "nymph", "fjord", "glyph", "crypt",
    "vexed", "jazzy", "waltz", "blitz", "whisk",
    "cynic", "knack", "quirk", "epoch", "abyss",
    "havoc", "ivory", "manor", "plume", "wrath"
]



# Main Function: Displaying the game rules and selecting the difficulty

def main():
    print("\t===============Welcome to Wordle!======================")
    print("\trules: Gues the 5 character word correctly in 5 tries")
    print("\t1. If a character is correctly placed it will show up as is"
        "\n\t\texample: w,o,r,d,l,e")
    print("\t2. If a character exist in the word = '*'"
        "\n\t\texample: *,o,r,d,l,e")
    print("\t3. If a character does not exist in the word = '-'"
        "\n\t\texample: -,o,r,d,l,e")
    print("\t4. guess the word correctly with these hints to win!!")
    print("\t=======================================================\n")
    
    while True:
        difficulty = input("Choose difficulty (easy/medium/expert): ").lower()
        if difficulty == 'easy':
            return easy_words
        elif difficulty == 'medium':
            return medium_words
        elif difficulty == 'expert':
            return expert_words
        else:
            print("Invalid difficulty. Please choose easy, medium, or expert.")

# Returns difficulty of the word
def diff(x):
    if x in easy_words:
        return 'easy'
    elif x in medium_words:
        return 'medium'
    else:
        return 'expert'

#Global variables

result = main()
lock = tuple("hello")
running = True
history = []
currhistory = []
alphabet = list("abcdefghijklmnopqrstuvwxyz")

def logic():
    print("WAITING FOR INPUT...")
    while True:
        arr = input(f"Guess the word({len(lock)} characters) ({diff(lock)}): ").lower()
        if len(arr) < len(lock):
            print("Invalid input. Please enter a word of the correct length.")
            continue
        else : break
        
    print("RECEIVED:", arr)
    abslist = list(arr)
    list2 = []
    curr = ['-', '-', '-', '-', '-']
    
    for i in range(5):
        list2.append(abslist[i])
        
    for i in range(len(list2)):
        if curr[i] == lock[i]:
            continue
        elif list2[i] == lock[i]:
            curr[i] = list2[i]
        elif list2[i] in lock:
            curr[i] = '*'
        else: curr[i] = '-'
    
    for i in curr:
        if i in alphabet:
            if i in curr:
                alphabet[alphabet.index(i)] = i.upper()
            else: alphabet[alphabet.index(i)] = '-'


    history.append(list2)
    currhistory.append(curr)
    for i in range(len(history)):
        print(f"Guess {i+1}:\t", end=" ")
        print(" ".join(history[i])," == Status:\t", " ".join(currhistory[i]))
        if i > 5:
            print("You have exceeded the maximum number of guesses.")
            return 1
    print("Current:\t ", end="")
    print(" ".join(list2))
    print("Best Guess:\t", end=" ")
    print(" ".join(curr)+"\n")
    print(" ".join(alphabet))

    if curr == list(lock):
        return "success"
    
        
while(running):
    result = logic()
    if result == "success" or result == 1:
        running = False
