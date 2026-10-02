'''
TITLE: sets.py
Description: Toy program showcasing Python sets.
Author: Shiwansh Bind
Requirements: Python 3.0+
'''

print("=== Sets Demo ===")

# a set keeps only unique items, no repeats, no order
marks = [10, 20, 20, 30, 30, 30]
print("List with repeats:", marks)
print("As set (repeats gone):", set(marks))

a = {"apple", "banana", "mango"}
b = {"banana", "mango", "orange"}
print("Set A:", a)
print("Set B:", b)

# add() puts one item, discard() removes one item safely
a.add("kiwi")
print("A after add kiwi:", a)

a.discard("apple")
print("A after discard apple:", a)

# len() counts, 'in' checks membership
print("Size of A:", len(a))
print("Is 'banana' in A?", "banana" in a)

# | is union (everything), & is common, - is only in left
print("A union B (all):", a | b)
print("A intersection B (common):", a & b)
print("A difference B (only in A):", a - b)
