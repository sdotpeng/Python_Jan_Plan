'''Yixin Li
CS151 B
Lab 2
Jan 20, 2021'''
'''The file contains functions that can build triangles and triangle stacks'''

import turtle
screen = turtle.Screen()
t = turtle.Turtle()

'''Function of a triangle'''
def triangle(side_length): # draw triangle with parameter: side_length
    t.forward(side_length)
    t.left(120)
    t.forward(side_length)
    t.left(120)
    t.forward(side_length)
# triangle(100) # main code

# '''Function of goto'''
# def goto(x, y): # set turtle to position (x, y)
#     print('goto(): going to', x, y)
#     print('goto(): before move, turtle at', turtle.position())
#     t.penup()
#     t.setposition(x, y)
    # t.setheading(0)
#     t.pendown()
#     print('goto(): after move, turtle now at', turtle.position())
# goto(200,10)
# triangle(100)
# goto(300,200)
# triangle(100)


def triangle2(x, y, scale):
    '''Draws a triangle at any (`x`, `y`) position and scale (`scale`)
    By default, the side lengths are 100 (when `scale` = 1)'''
    t.penup()
    t.goto(x,y)
    t.setheading(0)
    t.pendown()
    triangle(100 * scale)



def triangleStack(x, y, scale):
    '''Draws three triangles on top of each other.
    Smaller triangles are placed on top of larger ones
    '''
    # Largest triangle
    triangle2(x, y, 2 * scale)
    # Medium triangle in middle
    triangle2(x + 50, y + 173.2, 1 * scale)
    # Small triangle on top of stack
    triangle2(x + 75, y + 259.81, 0.5 * scale)

triangleStack(-200,0,1)
triangleStack(0,0,1/2)
triangleStack(200,0,1/3)


screen.exitonclick()