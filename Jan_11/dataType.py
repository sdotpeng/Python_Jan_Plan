# type() function can be used to tell us the data type of a value

# type()
def myType(object):
    return type(object)

print("Type of 1 is: ", type(1))
print("Type of 3.14 is: ", type(3.14))
print("Type of 'haha' is:", type('haha'))
print("Type of True is: ", type(True))
print("Type of 'True' is: ", type('True'))

print("------------------------")
print("Type of myType() is: ", type(myType))