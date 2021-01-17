# The return values, the return keywords, and multiple assignment

# Returning values from function
import math
def distance(x, y):
    dist = math.sqrt(x ** 2 + y ** 2)

# f(x) x is input, and the value of f(x) is the returning value
dist = 0
x = 3
y = 4
distance(x, y)
print(dist)

# dist is not changed, and its value computed in the function disappears. How do we get the value to live on?

# The return keyword
def distance(x, y):
    dist = math.sqrt(x ** 2 + y ** 2)
    return dist

dist = 0
x = 3
y = 4
dist = distance(x, y)
print(dist)

# A VERY common error: attempting to assign a vlue from a function that DOES NOT return a value
def distance(x, y):
    dist = math.sqrt(x ** 2 + y ** 2)

z = distance(x, y)

# There is no return statement, so distance has nothing to assign to the variable z in the main code

# Python tries its best to avoid crashing and assigns z a special value called None
print(type(z))

# Python keeps executing the rest of the program

# None Type
# You can actually assign variables of your own to None
myVar = None

# After learning conditionals, we can check if a variable is set to None
if z is None:
    pass

# Or use print
print(z)

# Same problem happens if you try to assign a value to a function call that has an empty return statement
def distance(x, y):
    return

z = distance(x, y)

# multiple assignment
a = 1
b = 1000000
# Your code here
print(a) # prints 1000000
print(b) # prints 1

# introducing the third variable
c = a
a = b
b = c

print(a, b)

a, b = b, a

# Tuple unpacking
a, b = (b, a)

# Multiple values returned
def advanced_division(numerator, denominator):
    quotient = numerator // denominator
    modulus = numerator % denominator
    return quotient, modulus

print(advanced_division(10, 3))
print(type(advanced_division(10, 3)))

# Multiple variable assignment
m, n = 100, 99

quotient, modulus = advanced_division(10, 3)
print("Quotient:", quotient)
print("Modulus:", modulus)