'''
TITLE: strings.py
Description: Toy program showcasing Python strings.
Author: Shiwansh Bind
Requirements: Python 3.0+
'''

print("=== Strings Demo ===")

# input() always gives us a string
name = input("Enter your name: ")
print("Hello,", name)

# len() counts characters
print("Your name has", len(name), "characters")

# strip() removes extra spaces
messy = "   hello python   "
print("Before strip:", messy)
print("After strip:", messy.strip())

# lower() and upper() change case
print("Lowercase:", name.lower())
print("Uppercase:", name.upper())

# replace() swaps one word for another
sentence = "I like apples"
print("Before:", sentence)
print("After:", sentence.replace("apples", "mangoes"))

# split() turns a string into a list
words = "apple banana mango".split()
print("Split into list:", words)

# join() turns a list back into a string
print("Joined with commas:", ", ".join(words))

# slicing means cutting out a part [start:end]
word = "python"
print("First 3 letters:", word[0:3])
print("Last 3 letters:", word[-3:])

# 'in' checks if something exists inside
print("Is 'py' in 'python'?", "py" in word)
print("Is 'java' in 'python'?", "java" in word)

# f-strings let us mix text and variables easily
print(f"Nice to meet you, {name.strip()}!")
