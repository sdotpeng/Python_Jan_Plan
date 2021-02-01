'''string.py
Demonstrate string properties. NOTE Make sure that you understand what everything does
'''

print(type('str'))

'''
<class 'str'>
'100' is an object/instance of the class 'str'
Every object of an class has attributes and methods defined from the class
'''

'''Escape sequences'''
# New line: \n
print('1')
print('')
print('1')

haiku = 'Haikus are easy.\nBut sometimes they don\'t make sense.\nRefrigerator'
print(haiku)

# Tabs: \t
haiku = 'Haikus are easy.\tBut sometimes they don\'t make sense.\tRefrigerator'
print(haiku)

haiku = '\t\tHaikus are easy.\n\t\tBut sometimes they don\'t make sense.\n\t\tRefrigerator'
print(haiku)

# Quote in strings: \' or \"
# Mixed quotation symbols also work (NOTE recent version of Python only)
haiku = "Haikus are easy. But sometimes they don't make sense. Refirgerator"
print(haiku)

# How to type backslash?
# print('Here is a backslash: \') NOTE does not work
myString = 'Here is a backslash: \\'
print(myString)

''' Length '''
print(len('haiku'))

''' String operators '''
# Concatenation: + operator with two strings
one = 'bat'
two = 'woman'
three = one + two
print(three)

# Replication: * operator with one string and one int
one = 'bat'
print(one*10)

# NOTE
# Accessing single characters
one = 'bat'
print('First letter is', one[0])
print('Last letter is', one[-1])

print(one[::-1])
print(one[::-2])

# Loop through a string like a list of characters:
for letter in 'batman':
    print(letter)

# Accessing ranges of characters (substrings)
# We can slice strings like lists, but we can't use assignment to replace
# characters or substrings
# Let's access 'bat' in 'batman'
print('First word in batman', three[0:3])
print('Last word in batman', three[-3:0])

'''Substrings'''
# Determine whether a string (the substring) appears / doesn't appear inside another one
# Text: 'two wrongs don\'t make a right'
# Text: 'right'
a = 'two wrongs don\'t make a right'
b = 'right'
print('Is "right" in the bigger string?', b in a)
print('Is "right" not in the bigger string?', b not in a)

'''Iterating through strings'''
# We can iterate through strings, not just range() and lists:
# Text: 'Hello World'
myString = 'Hello World'
for letter in myString[:5]:
    print(letter)