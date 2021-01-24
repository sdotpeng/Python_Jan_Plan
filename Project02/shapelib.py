'''
Yixin Li
CS151 B
Lab_2
Jan 20, 2021
'''
'''The file works as a shape library for the project'''

import turtle
# screen = turtle.Screen()
# t = turtle.Turtle()
import random

'''Function of a triangle'''
def triangle(t, side_length): # draw triangle with parameter: side_length
    t.forward(side_length)
    t.left(120)
    t.forward(side_length)
    t.left(120)
    t.forward(side_length)
# triangle(100) # main code

'''Function of goto'''
def goto(t, x, y): # set turtle to position (x, y)
    t.penup()
    t.setposition(x, y)
    t.setheading(0)
    t.pendown()

'''Function of creating triangle2'''
# create triangle with parameters: x, y, and scale
'''Draws a triangle at any (`x`, `y`) position and scale (`scale`)
    By default, the side lengths are 100 (when `scale` = 1)'''
def triangle2(t, x, y, scale):
    goto(t, x, y)
    t.fillcolor()
    t.begin_fill()
    triangle(t, 100 * scale)
    t.end_fill()


'''Function drawing three triangles on top of each other.
    Smaller triangles are placed on top of larger ones'''
def triangleStack():
    # Largest triangle
    triangle2(0, 0, 2)
    # Medium triangle in middle
    triangle2(50, 173.2, 1)
    # Small triangle on top of stack
    triangle2(75, 259.81, 0.5)

'''Function drawing three triangles on top of each other with scale'''
def triangleStack(t, x, y, scale): # scale works like a default length
    goto(t, x, y)
    triangle2(t, x, y, scale * 2)
    triangle2(t, x + scale * 50, y + scale * 173.2, scale * 1)
    triangle2(t, x + scale * 75, y + scale * 259.81, scale * 0.5)

# triangleStack(-200, 0, 1)  # draw three stacks of triangles
# triangleStack(0, 0, 1/2)
# triangleStack(100, 0, 1/3)

''' Function of creating a triangle'''
def rectangle(t, x, y, length, width): # length and width can later be displayed with scale
    goto(t, x, y)
    t.forward(length)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(width)

'''Function of creating a circle with fillcolor'''
def circle(t, x, y, arc_length, color1):
    goto(t, x, y)
    t.speed(10)
    t.pencolor(color1)
    t.fillcolor(color1)
    t.begin_fill()
    for times in range(360):
        t.forward(arc_length)
        t.left(1)
    t.end_fill()
# circle(100, 10, 1, 'purple')
# circle(0, 0, 2, 'red')
# circle(150, -300, 3, 'blue')

'''Function of creating a star shape'''
# length can later be displayed with scale
def star(t, length):
    for times in range(5):
        t.forward(length)
        t.right(144)

'''Function of creating a star shape with scale'''
def star2(t, x, y, scale):
    # start point = (x,y)
    goto(t, x, y)
    star(t, 100 * scale)

'''Function of creating a rectangle with scale'''
def rectangle2(t, x, y, scale):
    goto(t, x, y)
    # set default value to scale
    rectangle(t, x, y, 100 * scale, 200 * scale)

def rectangle3(t, x, y, scale, color):
    goto(t, x, y)
    t.fillcolor(color)
    t.begin_fill()
    # set default value to scale
    rectangle2(t, x, y, 100 * scale, 200 * scale)
    t. end_fill()

def oval(t, x, y, r, color1, color2):
    t.pensize(4)
    goto(t,x,y)
    t.pencolor(color1)
    t.fillcolor(color2)
    t.begin_fill()
    t.setheading(315)
    t.speed(10)
    for loop in range(2):
        t.circle(r * 2,90)
        t.circle(r/18,90)
    t.end_fill()
# oval(t, 0, 0, 60, 'DimGrey', 'LightSlateGrey')

'''Function of creating compound shape1: meteor'''
def meteor(t, x, y, scale, color):
    goto(t, x, y)
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    # star2 with different scale and offset can create a compound shape
    star2(t, x, y, scale * 2)
    star2(t, x + scale * 200, y + scale * 0, scale * 1)
    star2(t, x + scale * 300, y + scale * 0, scale * 0.5)
    rectangle2(t, x + scale * 350, y + scale * 0, scale * 1/3)
    t.end_fill()
# meteor(t, -200, 0, 1, 'yellow')
# meteor(t, -200, 100, 1/2, 'orange')
# meteor(t, -200, 200, 1/3, 'GreenYellow')

'''Function of creating compound shape2: rocket'''
def rocket(t, x, y, scale, color):
    goto(t, x, y)
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    triangle2(t, x, y, scale * 1)
    triangle2(t, x + scale * 25, y + scale * 86.61, scale * 0.5)
    rectangle2(t, x + scale * 0, y + scale * 0, scale * 1)
    star2(t, x + scale * 0, y + scale * -238.2, scale * 1)
    t.end_fill()
# rocket(t, -200, -100, 1/2, 'red')
# rocket(t, -50, 0, 1/3, 'blue')
# rocket(t, 100, 100, 1/4, 'purple')

def spaceship(t, x, y, scale):
    t.speed(10)
    goto(t,x,y)
    circle(t, x, y, 1 * scale, 'tomato')
    oval(t, x - 80 * scale, y + 80 * scale, 60, 'DimGrey', 'LightSlateGrey')
    triangle3(t, x - 50 * scale, y + 80 * scale, 1, 'SteelBlue1')
# spaceship(t, 250, -250, 1)
# spaceship(t, 120, -200, 1)

# screen.exitonclick()