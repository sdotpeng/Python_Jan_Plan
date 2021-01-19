import turtle
window = turtle.Screen()
t = turtle.Turtle()

t.setpos(0, 0)
t.setheading(0)
def rhombus(color):
    t.color(color)
    t.begin_fill()
    t.left(140)
    t.forward(200)
    t.right(110)
    t.forward(200)
    t.right(70)
    t.forward(200)
    t.right(110)
    t.forward(200)
    t.end_fill()
rhombus('yellow')

t.setpos(0, 0)
t.setheading(0)
def heart(color):
    t.speed(400)
    t.color(color)
    t.begin_fill()
    t.left(140)
    t.forward(100)
    for times in range(200):
        t.right(1)
        t.forward(1)
    t.left(110)
    for times in range(200):
        t.right(1)
        t.forward(1)
    t.forward(100)
    t.end_fill()
heart('pink')

def shapeThree():
    t.setheading(237)
    rhombus('yellow')
    t.setheading(237)
    heart('pink')
    t.setheading(117)
    rhombus('yellow')
    t.setheading(117)
    heart('pink')
shapeThree()

t.penup
t.setposition(-50, 20)
t.setheading(0)
t.pendown

def shapeC(length, color, angle):
    t.color(color)
    for times in range(5):
        t.forward(length)
        t.right(angle)
shapeC(100, 'blue', 144)

t.speed(100)

def shapeD(length, color, angle):
    shapeC(length, color, angle)
shapeD(70, 'purple', 144)
shapeD(50, 'green', 144)
shapeD(30, 'red', 144)

window.exitonclick()