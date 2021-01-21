import turtle
s = turtle.Screen()
t = turtle.Turtle()

def square(t, x, y, scale):
    '''
    Draw a square at (x,y) with the given scale
    '''
    DEFAULT_LENGTH = 100
    t.up()
    t.goto(x, y)
    t.down()
    t.setheading(0)

    t.forward(scale * DEFAULT_LENGTH)
    t.left(90)
    t.forward(scale * DEFAULT_LENGTH)
    t.left(90)
    t.forward(scale * DEFAULT_LENGTH)
    t.left(90)
    t.forward(scale * DEFAULT_LENGTH)
    t.left(90)

square(t, 0, 0, 1)
square(t, 200, 200, 2)

s.exitonclick()