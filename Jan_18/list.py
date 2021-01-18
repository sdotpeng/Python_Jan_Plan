# List is a collection of elements in Python

# Why do we need list?

# turt1 = make_turtle()
# turt2 = make_turtle()
# turt3 = make_turtle()
# turt4 = make_turtle()

# turt1.move()
# turt2.move()
# turt3.move()
# turt4.move()

# turtles = [turt1, turt2, turt3, turt4]

import turtle
import random

'''Creating lists'''
# Items in list enclosed by square brackets [] and each item separated by a comma
my_list = [9, 99, -500, -1, 0]

# A list can hold items with a mix of any data types, including objects
# screen = turtle.Screen()
# turt = turtle.Turtle()
# my_list = [99, True, 'hi!', screen, turt]

# Use print to see what's in a list
print('Here is my list', my_list)

'''Accessing items'''
# You may also use square brackets to access items in the list
# Place them to the right of the list variable name and use an int to get the i-th item
# NOTE: Counting starts with 0, not 1 -> 1st item at position 0, 2nd item at position 1
# Get the 1st, 2nd, and 4th items
print(my_list[0])
print(my_list[1])
print(my_list[3])

# NOTE: These ints that tell us the position in the list we want to access an
# item is called an INDEX

# You can assign an item (after you access it) to a new variable
myNumber = my_list[2]
print(myNumber)

# If you need to access items near the end of the list? Use negative indices
# Print out the last and 2nd last items
print(my_list[-1])
print(my_list[-2])

'''How many items do I have in a list?'''
# Use the `len` function to get the length of the list (how many items it has)
print(len(my_list))

# NOTE: You can also use my_list[len(my_list)-1] to access the last element

'''Slicing'''
# You can access multiple items in a list and get a smaller list back using slicing
# Slicing uses 1 or 2 colons inside the square brackets
# Use slicing to access and print the first 3 elements in a list
numList = list(range(10))
first1 = numList[0:1]
print(first1)
first3 = numList[0:3]
print(first3)

# NOTE: Position of int BEFORE: is INCLUDED. Position of int AFTER: EXCLUDED

# Tricks: You can omit index before or after colon if position of beginning or end of list included
# Print the 1st and last three elements
print(numList[:3])
print(numList[-3:])

# Print every other item in a list (all items excluding the last one)
print(numList[0:len(numList)])

print(numList[0:-1])
print(numList[0:-1:2])
print(numList[::2])

# Reverse a list (make back front, make front back) using negative step value
numList = list(range(10))
print(numList[::-1])

'''Looping through a list'''
# Until now, we've been using range to write a for loop
# for i in range(10):
#   print(i)
# What is range? Range actually acts like a list
# Let's force range to reveal itself as a list:
print(list(range(10)))

# So when we write a loop with range, it's eseentially using a list like this:
# for i in [0,1,2,3,4,5,6,7,8,9]:
#   print(i)

# We can loop through any list by replacing range with the list
# NOTE: The loop variable (i.e. the loop index) becomes each item, not the iteration number!
lst = [4,2,10]
for i in lst:
    print(i)

lst = ['a', 'b', 'c']
for letter in lst:
    print(letter)

screen = turtle.Screen()
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()
input("Press Enter...")
turtles = [t1, t2, t3, t4]
for turtle in turtles:
    turtle.goto(600 * random.random() - 300, 600 * random.random() - 300)

screen.exitonclick()