# Conditionals is a basic control flow in Python

# if statement

# if [boolean condition statement]:
#   <conditional body>

# If there's traffic, then we want to take a different route. If it's raining, go outside with
# and umbrella.

# The boolean condition MUST evalute to True to enter the if statement body

rains = True

if rains:
    stayHome()
else:
    goOut()

rains = 'None'

if rains == 'None':
    goOut()
elif rains == 'Light':
    doSth()
elif rains == 'Heavy':
    doSth2()
else:
    stayHome()

# For a conditional in Python, only 'if' is mandatory, 'else' and 'elif' are optional

if turtle.heading > 0:
    pass

# There are multiple ways to evalute a True or False statment
# if <true condition>:


True/False
2.0 > 0
# >
# <
# >= greater than or equal to
# <= less than or equal to
# == equal to
# != not equal to

# and operation
# True and True -> True
# True and False -> False
# False and True -> False
# False and False -> False

# or operation
# True or True -> True
# True or False -> True
# False or True -> True
# False or False -> False

# not operation
# not True -> False
# not False -> True

# if 2.0 > 0 and 3.0 < 5:
# if isRaining():

# def isRaining():
#       return <boolean value>

# if 2.0 < 0 or isRaining():

# if isRaining() and carryUmbrella() or hasACar():

# Lazy evaluation
# If there is more than one of the same compound boolean operator in a condinitional statement
# Python always evaluates left-to-right

# In a long string of and conditions, Python stops checking and considers the entire expression False
# if it encounters one False:

if a and b and c and d and e and f and g:
    print('yes')

# If a is False, Python does not even bother checking b, c, d, e, etc.

# In a long string of or conditions, Python stops checkinng and considers the entire expression 
# True if it encounters one True

if a or b or c or d or e or f:
    print('yes')

# If a is True, Python does not even bother checking b, c, d, e, etc.