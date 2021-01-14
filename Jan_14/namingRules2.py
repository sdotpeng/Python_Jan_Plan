# Rule 1: Variables may only contain upper case letter (A-Z), lower case (a-z)
# decimal digits (0-9), and the underscore character (_)

# Spaces aren't allowed - (my variable = 10) is an invalid variable assigment
# Other punctuation is not allowed (myVariable#, mine&yours are not allowed)

# Rule 2: A variable must start with an upper or lower case letter
# While upper case first letters are valid, we use by convention a lowercase to start

# Rule 3: Any variable name cannot contain reserved words (keywords) by Python.
# For example, you cannot name a variable 'for' because Python wouldn't know if you meant
# variable 'for' for wanted to define a loop
# Others include False, None, True, import and return

# Variable assignment
myAssignedVariable = 10

# Variables can change value
myAssignedVariable = 11
print(myAssignedVariable)

myAssignedVariable = 0
for i in range(10):
    myAssignedVariable = myAssignedVariable + 1

print(myAssignedVariable)

# The loop index is also a variable
for i in range(5):
    print(i ** 2)

# Avoid changing the value of loop index inside a loop
for i in range(5):
    i = i + 1
    print(i)

for i in range(5):
    value = i
    print(value + 1)