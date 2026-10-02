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

| # | Program               | Source Code                               |
|---|-----------------------|-------------------------------------------|
| 1 | A Simple Calculator   | [calc.py](#1-a-simple-calculator-calcpy)  |
| 2 | Wordle clone game     | [Wordle.py](#2-wordleclone-game-wordlepy) |
| 3 | Guess The Number      | [guess.py](#3-guess-the-number-guesspy)   |
| 4 | Rock Paper Scissors   | [rps.py](#4-rock-paper-scissors-rpspy)     |
| 5 | GK Quiz               | [quiz.py](#5-gk-quiz-quizpy)              |
| 6 | Dice Roller           | [dice.py](#6-dice-roller-dicepy)          |
| 7 | Strings Demo          | [strings.py](#7-strings-demo-stringspy)   |
| 8 | Numbers Demo          | [numbers.py](#8-numbers-demo-numberspy)   |
| 9 | Lists Demo            | [lists.py](#9-lists-demo-listspy)         |
| 10 | Sets Demo            | [sets.py](#10-sets-demo-setspy)           |

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

### 3. Guess The Number [guess.py](/programs/guess.py)

similar fun to wordle but with numbers. computer picks 1-20 and you keep guessing, it tells you too high / too low and hot / warm / cold.

uses while loop and if-else and a list to remember all tries.

---

### 4. Rock Paper Scissors [rps.py](/programs/rps.py)

classic game vs computer. you type rock / paper / scissors and it keeps score.

uses a list for choices and random.choice() to pick for computer, nothing fancy.

---

### 5. GK Quiz [quiz.py](/programs/quiz.py)

5 tiny questions, type answer and it says correct / wrong and gives score / 5 at end.

mostly just input() + if-else and .strip().lower() so caps and spaces dont matter.

---

### 6. Dice Roller [dice.py](/programs/dice.py)

press enter to roll 2 dice. same number = doubles you win, 7 or 11 = lucky.

uses random.randint(1, 6) and a while loop to keep rolling.

---

### 7. Strings Demo [strings.py](/programs/strings.py)

strings are way easier than char arrays in c. no strlen / strcmp nonsense.

```python
name.lower() # SHIWANSH -> shiwansh
"a,b,c".split() # becomes ['a', 'b', 'c']
"py" in "python" # True, no loop needed
```

covers strip / lower / upper / replace / split / join / slicing.

---

### 8. Numbers Demo [numbers.py](/programs/numbers.py)

int and float stuff. enter 2 numbers and it does all operations at once.

```python
10 // 3 # = 3, whole part only
10 % 3  # = 1, remainder
10 ** 2 # = 100, power
```

also round() / abs() / min() / max() / type().

---

### 9. Lists Demo [lists.py](/programs/lists.py)

list is like 1-D array but it can grow and shrink. my favourite coming from c.

```python
fruits.append("orange") # adds at end
fruits.pop(0) # removes by position
"mango" in fruits # True, no for loop
```

covers append / extend / insert / remove / pop / sort / reverse.

---

### 10. Sets Demo [sets.py](/programs/sets.py)

set is just a list with no repeats and no order. good for removing duplicates.

```python
set([10, 20, 20, 30]) # = {10, 20, 30}
a | b # union, everything
a & b # intersection, only common
a - b # difference, only in a
```

covers add / discard / union / intersection / difference.

---
