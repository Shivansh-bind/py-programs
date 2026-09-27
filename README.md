# Functional Python Toy Programs

For educational purpose (no non venomous snake was harmed during the making of this repository)

    I made as a previously c and c++ coder

    This is my first attempt at python programming.
    
    I used to code in c so it was pretty jarring to try something with so many abstractions.
    
    my experience with c and c++ did not make the learning any easier in fact i would argue it made it harder for me.

    the kind of practices i used to follow when writing c or c++ don't apply here.

```python
def main(): # Declaring the function and defining it.
    statements # statements that are to be executed.
main() # <-- this is different as we are calling the main function. 

#In c or c++ it is the default and first function that is called which is not the case in python you have to manually call it if declared its not even necessary to create a function.
```

while python has many quirky behaviours and has a bad rep in low level programming circles it is still the king of automation and AI/ML/DS/ and many other fields due to being **super beginner friendly** as you know it follows an english like syntax its basically english.

```python
    #to check if a string exists in a list 
    if 'hello' in list1:
        print("yes")

    #to check if a string does not exist in a list
    if 'bye' not in list1:
        print("bye does not exist")
```

I found this really funny as comparing lists(1-D array) is so easy now instead of checking each element like arr[i] == arr1[i] uning ***in*** and ***not in***

## Table of contents

| # | Program               | Source Code                                  |
|---|-----------------------|----------------------------------------------|
| 1 | A Simple Calculator   | [calc.py](#1-a-simple-calculator-calcpy)     |
| 2 | Wordle clone game     | [Wordle.py](#2-wordleclone-game-wordlepy)    |
| 3 | Student management    | [sms.py](#3-student-management-system-smspy) |

---

### 1. A Simple Calculator [calc.py](/programs/calc.py)

Mostly clean structure and no unnecessary junk, simple python program that performs calculations on a given set of values(float).

prompts the user to enter 2 operands to perform calculations on:

```python
# here we use input("prompt") function 
# it features built in println function to prompt the user for input
# float() is also a function 
# which wraps input() to convert the input into a floating point precision value basically rational numbers 

a = float(input("Enter the 1st operand: "))
b = float(input("Enter the 2nd operand: "))
```

---

### 2. Wordle(clone) Game [Wordle.py](/programs/Wordle.py)

![Wordle showacase](/programs/showacases/Wordle.gif)

---

### 3. Student Management System [sms.py](/programs/sms.py)

---
