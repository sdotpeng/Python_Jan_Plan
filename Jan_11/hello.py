# This code prints Hello World on the output field
print('Hello World!')

# Function
# f(x) is mathematical function, where the input is x,
# and the output is the value of f(x)
# y = x^2, where input is x and output is x^2

# Function in Python is also a processor where you input
# none or multiple values and return none or multiple values

# Function makes it easy to automate and do a sequence of actions
# whenever we want

# In multivariate calculus, we have function like F(x, y) where
# there are two allowed inputs

# Zero argument
def morningRoutine():
    getOutOfBed()
    brushTeeth()
    washFace()
    getDressed()
    sayMorningToRicky()
    haveBreakfast()
    # codes here
    return None

def getOutOfBed():
    sitUp()
    standUp()
    wearShoes()

# One argumnet
def morningRoutine(breakfastChoice):
    getOutOfBed()
    brushTeeth()
    washFace()
    getDressed()
    sayMorningToRicky()
    haveBreakfast(breakfastChoice)
    # codes here
    return None

# Function f(x) = x^2 can be written as
def f(x):
    return x ** 2

# Calculate the size and perimeter of a square

def calculateSqaure(length):
    # It actually returns a tuple instead of multiple values
    return length * length, 4 * length

calculateSqaure(8)

morningRoutine('Continential')
morningRoutine('Chinese')

# Multiple arguments
def morningRoutine(breakfastChoice, dressChoice):
    getOutOfBed()
    brushTeeth()
    washFace()
    getDressed(dressChoice)
    sayMorningToRicky()
    haveBreakfast(breakfastChoice)
    # codes here
    return mood

# Below is the template of a Python method/function
def funcname(parameter_list):
    """
    docstring
    """
    pass

# Data Types

# Integer or int in Python
1
88

# Float or float in Python
1.0
88.111
3.14159

# String or str in Python
'Yixin Li'
'Colby College'
'a'

# In Java, people differntiate char with str
# 'A' is a char
# "Aa" is a string

# In Python, both '' and "" can be used to quote a string
'a'
"a"

# Boolean 布尔 Boole
True
False