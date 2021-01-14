# Compiler & Interpreter

# In Java or most other languages, we use compiler that compiles
# an entire program and run

# By in Python, the interpreter allows us to interpret codes line by line

# print(10)
# print('Here')
# print(3 / 0)

# def function():
#     print("Here in function")
#     print(3/0)

# # function()

# Operators and precedence

# Integer and Float
# print(2 + 2)

# print(2 ** 4)

# print(2 - 4)

# print(2 * 4)

# print(2 / 4)

# print(5 / 3)

# # Floor division operator
# print(5 // 3)

# # 5 / 3 = 1 ... 2

# # Remainder operator (modulus)
# print(5 % 3)

# # A function that returns an absolute value of the given argument
# print(abs(-1))

# Module/Package
# import math
# # moduleName.funcName()
# # moduleName.classname.funcName()
# math.exp(math.e)

# math.cos(0)
# math.sin(1)
# math.sqrt(9)
# math.sin(math.pi)
# math.sin(math.sqrt(1))
# f(g(x))

import random

# This function will generate a random float between 0 and 1 (exclusive)
print(random.random())

# How will we generate a random integer?

# print(random.randint(1, 5))

# name = input("Enter your name: ")

# print("Welcome to Python, ", name, name, 18)

# String concatenation

# welcome_message = "Welcome to Python, "
# output = welcome_message + name
# print(output)

# Data Type Compatibility
print(2 + 3)
print("Welcome" + " Yixin")
# print(2 + "Yixin")
print(str(2) + "Yixin")
print('2' + '3')

print(2 * "Yixin")
print('456' * 10)

# Type Conversion
# Example comparing an int and a float
print(4.0 * 3)
print(4 * 3)

apple_price = 4.5
print(int(apple_price * 2))

# Converting may result in information loss
print(int(3.9))
print(3.9 ** 3)
print(3 ** 3)

# There are several types of converting functions
# int(), str(), float(), bool()

# Use round to get a better converted integer
print(round(3.9))
print(round(3.1))