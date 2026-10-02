'''
TITLE: numbers.py
Description: Toy program showcasing Python numbers (int and float).
Author: Shiwansh Bind
Requirements: Python 3.0+
'''

print("=== Numbers Demo ===")

# float() converts input into decimal numbers
a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))

# basic arithmetic
print(f"{a} + {b} =", a + b)
print(f"{a} - {b} =", a - b)
print(f"{a} * {b} =", a * b)

# division: / gives float, // gives whole part, % gives remainder
print(f"{a} / {b} =", a / b)
print(f"{a} // {b} =", a // b)
print(f"{a} % {b} =", a % b)

# ** means power
print(f"{a} ** 2 =", a ** 2)

# type() tells us int or float
print("Type of a:", type(a))

# int() cuts off the decimal part
print("a as int:", int(a))

# round() keeps only few decimals
print("a rounded to 2 decimals:", round(a, 2))

# abs() removes minus sign, min() / max() pick smallest / biggest
print("Absolute of -5:", abs(-5))
print("Smallest of a and b:", min(a, b))
print("Biggest of a and b:", max(a, b))
