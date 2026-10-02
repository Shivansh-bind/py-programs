'''
TITLE: lists.py
Description: Toy program showcasing Python lists and its methods.
Author: Shiwansh Bind
Requirements: Python 3.0+
'''

print("=== Lists Demo ===")

# a list keeps many items in one box
fruits = ["apple", "banana", "mango"]
print("Start:", fruits)

# append() adds one item at the end
fruits.append("orange")
print("After append:", fruits)

# extend() adds many items at the end
fruits.extend(["grape", "kiwi"])
print("After extend:", fruits)

# insert() adds at a fixed place (index 1 = 2nd place)
fruits.insert(1, "cherry")
print("After insert at 1:", fruits)

# len() counts items, 'in' checks if item exists
print("Total fruits:", len(fruits))
print("Is 'mango' in list?", "mango" in fruits)

# indexing starts at 0, slicing cuts [start:end]
print("First fruit:", fruits[0])
print("First 3 fruits:", fruits[0:3])

# index() finds position, count() counts repeats
print("Position of 'mango':", fruits.index("mango"))
print("Count of 'apple':", fruits.count("apple"))

# remove() deletes by name, pop() deletes by position
fruits.remove("banana")
print("After remove banana:", fruits)

popped = fruits.pop(0)
print("Popped:", popped)
print("After pop:", fruits)

# sort() A-Z, reverse() flips order
fruits.sort()
print("Sorted:", fruits)

fruits.reverse()
print("Reversed:", fruits)
