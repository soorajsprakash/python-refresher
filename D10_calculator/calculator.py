# --------------------------------------------------------------
# ------------------ FUNCTIONS WITH OUTPUT ---------------------
# --------------------------------------------------------------

import os
from calculator_art import logo

# to clear interpreter
def clear():
	os.system('clear')

# Add
def add(a, b):
    return a+b
# Subtract
def subtract(a, b):
    return a-b
# Multiply
def multiply(a, b):
    return a*b
# Divide
def divide(a, b):
    return a/b

operations = {
    '+' : add,
    '-' : subtract,
    '*' : multiply,
    '/' : divide
}

def calculator():
    clear()
    print(logo)
    shouldContinue = True
    a = float(input("Whats the first number?: "))
    for key in operations:
            print(key)

    while shouldContinue:
        operationSym = input("Pick an operation: ")
        b = float(input("Whats the next number?: "))
        answerFunc = operations[operationSym]
        answer = answerFunc(a, b)
        print(f"{a} {operationSym} {b} = {answer}")
        Q = input("Press 'y' to continue with the answer or 'n' to start over: ").lower()
        if Q == 'n':
            shouldContinue = False
            calculator()
        elif Q == 'y':
            a = answer

calculator()


# -------- OLD STEPS ----------
# a = int(input("Whats the first number?: "))
# for key in operations:
#     print(key)
# operationSym = input("Pick an operation from the line above: ")
# b = int(input("Whats the second number?: "))
# answerFunc = operations[operationSym]
# firstAns = answerFunc(a, b)
# print(f"{a} {operationSym} {b} = {firstAns}")

# operationSym = input("Pick an operation from the line above: ")
# c = int(input("Whats the third number?: "))
# answerFunc = operations[operationSym]
# secAns = answerFunc(firstAns, c)
# print(f"{a} {operationSym} {c} = {secAns}")