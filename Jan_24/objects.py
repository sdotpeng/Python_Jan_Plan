# Objects
# New type of data: other than string/float/int/boolean
# objects are non-primitive data types

# NOTE: Two key ideas
# Objects can help us organize data/information related to a thing we care about
# ---> Objects know stuff
# Objects allow you to perform operations (actions) and manipulate the stored data
# ---> Objects can do stuff

car1_color = 'blue'
car1_tanksize = 11
car1_price = 40000
car2_color = 'silver'
car2_tanksize = 15

# The data here are not really associated with car1, car2... they are just names we campe up with
# Objects actually group together data related to an instance of a common thing
# Common thing here: Cars
# 2 cars -> 2 unique Car obejcts ("2 instances of a car"): Car 1, Car 2
# each instance only stores data relevant to itself.

car1.color = 'blue'
car2.tanksize = 15

# We can perform actions on objects to change their data
# Example: Car 1 gets painted gray, How do we tell the object that its existing
# color (blue) needs to change?

# We can call a function, passing in the new color (blue)
car1.setColor('gray') # setter

# How do we find out what Car 1 and Car 2's colors currently are?
# We can call another function on each object that returns the current color string.
color1 = car1.getColor() # getter
print(color1)

# Summary
# 1. Each object holds and groups togther info that makes that object unique
# 2. Call functions on the objects to do actions like set and get their unique data
# car1.getColor()
# 3. Functions called on objects called methods

# digits = [5,4,6,3,1,2]
# digits.sort()
# lst = sorted(digits)

# The unique object GOES BEFORE THE DOT (car1.func() vs. car2.func())
car1.getColor()
car2.getColor()

# turtle with objects
# Enable us to do cool things that weren't possible before
# Two things / types of objects we will work with
# Turtle: You can now create more than one turtle that draws on the screen!
# Each is an object and has unique properties (color, shape, position on canvas, pen width)
# t1 = turtle.Turtle() - we created an object called t1
# t1.penup(), t1.forward()
# t2.forward()
# Screen: represents the canvas (pop-up window in which tutrle draws stuff)
# Controls canvas size, background color, etc

# How do we create objects in the first place?
# Call a special method called the constructor, It returns a new object
# NOTE constructor normally starts with a capital letter
# Screen()
# Turtle()
# To create two Turtle objects to draw stuff (later)
# turt1 = turtle.Turtle()
# turt2 = turtle.Turtle()
# The two objects are independent: changing tutr1's color will not affect turt2