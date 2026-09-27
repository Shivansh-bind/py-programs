'''
TITLE: Simple-calculator.py
Author: Shiwansh Bind
Github: [github.com/shivansh-bind](http://github.com/shivansh-bind)
Requirements: Tested on Python 3.14.7+ ; might work on older versions 3.0+
Version: 0.0.12
'''

def welcome():
    print("\n==============================")
    print("Welcome to a Simple Calculator")
    print("==============================\n")


def calc(x, y, choice):
    if choice == '+':
        return x + y

    elif choice == '-':
        return x - y

    elif choice == '*':
        return x * y

    elif choice == '/':
        if y == 0:
            return "Cannot divide by zero"
        return x / y

    else:
        return "ERROR! 404 Bad Request"


def main():
    oplist = ['+', '-', '*', '/']
    running = True
    while running:
        a = float(input("Enter the 1st operand: "))
        b = float(input("Enter the 2nd operand: "))
    
        print(
            "List of Operations:\n"
            "Addition \t=  +\n"
            "Subtraction \t=  -\n"
            "Multiply \t=  *\n"
            "Divide \t\t=  /\n"
            "Your choice",
            end=":"
        )
    
        while True:
            choice = input()
    
            if choice in oplist:
                break
            else:
                print("Invalid input!!\nre-enter the Operation: + - * / ", end=": ")
    
        print(f"{a} {choice} {b}", end=" = ")
        print(calc(a, b, choice))
        
        while True:
            running = input("Do you want to continue? (y/n): ")
            
            if running.lower() in ['y', 'n']:
                break
            else:
                print("Invalid input!!\nre-enter the choice", end=": ")

        if running.lower() == 'n':
            running = False

if __name__ == "__main__":
    welcome()
    main()