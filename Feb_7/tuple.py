'''tuple.py
First touch on tuple
'''

lst = [1,2,3]
tp = (1,2,3)

print(lst[1:2])
print(tp[1:2])

# tp[2] = 1

print(type((2)))
print(type((2,)))

tuple(lst)

tuple.count(1)
tuple.index(3)

# Why do we need tuple?
#   1. Tuple unpacking - multiple returning values
#   2. Can be used as key-value pair in python dictionaries
#   3. As a return value from database