'''mutable.py
The difference between mutable and immutable types
'''

# A list is a mutable type
a = [1,2,3,4]

# I can use the variable assignment notation to change the value of one element in the list
a[0] = 100

# We can also use insert() method to change the value of list `a`
a.insert(3, 200)

a.sort()

# String is an immutable type
s = 'hello world'
# s[0] = 'm'
s = s.replace('world', 'Mars')
print(s)

'''
Review:

Mutable types: list, dictionary, set, user defined objects
Immutable types: integer, float, long, complex, string, tuple
'''

