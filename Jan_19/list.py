# When we want to loop through multiple lists at once, it is easiest to use range with an index
# Let's move back the turtles back to the origin and move them to the following coordinates

# x = [-200, -100, 100, 200]
# y = [200, 100, -100, -200]
# colors = ['red', 'blue', 'pink', 'orange']

# import turtle
# screen = turtle.Screen()
# t1 = turtle.Turtle()
# t2 = turtle.Turtle()
# t3 = turtle.Turtle()
# t4 = turtle.Turtle()
# input("Press Enter...")
# turtles = [t1, t2, t3, t4]

# for i in range(len(turtles)):
#     print(i)
#     turtles[i].goto(0, 0)
#     turtles[i].color(colors[i])
#     turtles[i].goto(x[i], y[i])


# screen.exitonclick()

'''Adding/updating/removing items from an existing list'''
import turtle


lst = [1,2,3,4,5]
# You can use variable assignment to update one item of a list at a time
myNumList = list(range(5))
myNumList[1] = 99
print(myNumList)

# Let's use this to update a list with 2 added to every item in the list
for i in range(len(myNumList)):
    myNumList[i] = myNumList[i] + 2
print(myNumList)

# There are TWO VERY IMPORTANT methods for lists, and one less common, but still good to know
# append(): useful to building a list. It adds item to the end of a list
my_list = []
my_list.append(10)
print(my_list)

# myTurtles = list()
# for i in range(4):
#     turt = turtle.Turtle()
#     myTurtles.append(turt)

# pop(): remove items from the END of the list. "Undo" what append does
# Pop off a few items from my_list
my_list = []
my_list.append(10)
my_list.append(99)
my_list.append(55)
print(my_list)
my_list.pop()
print(my_list)
var = my_list.pop()
print(my_list)
print(var)

# insert(): Lets you add an item at a position in the list
# There are two parameters: <list>.insert(<position>, <thing to insert>)
my_list = list(range(5))
print(my_list)
print(my_list[2])
my_list.insert(2, 999)
print(my_list)

'''Containment'''
my_list = list(range(5))

print(4 in my_list)
print(6 in my_list)

print(5 not in my_list)

# clear(): removes all the elements from the list
my_list = list(range(5))
my_list.clear()
print(my_list)

# count(): Returns the number of elements with the specified value
my_list = list(range(5))
print(my_list.count(1))
my_list = [5, 5, 4] * 3
print(my_list)
print(my_list.count(4))
print(my_list.count(0))

# index(): returns the index of the first element with the specified value
my_list = [3,4,1,2,3]
print(my_list.index(1))
print(my_list.index(3))
# print(my_list.index(0))

# remove(): removes the first item with the specified value
my_list = list(range(5))
my_list.append(4)
print(my_list)
my_list.remove(4)
print(my_list)

# reverse(): reverses the order of the list
my_list = list(range(5))
print(my_list)
my_list.reverse()
print(my_list)

# sort(): sorts the list
import random
my_list = []
for i in range(10):
    my_list.append(random.randint(1,100))

print(my_list)
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)

