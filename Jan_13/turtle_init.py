import turtle
Yixin = turtle.Turtle()
Yixin.forward(100)
Yixin.backward(100)
Yixin.position()
Yixin.pos()
Yixin.forward(200)
Yixin.pos()
Yixin.forward(-200)
Yixin.left(45)
Yixin.heading()
Yixin.right(45)

def triangle():
    Yixin.forward(200)
    Yixin.left(120)
    Yixin.forward(200)
    Yixin.left(120)
    Yixin.forward(200)

triangle()
Yixin.left(120)
def triangle(length):
    Yixin.forward(length)
    Yixin.left(120)
    Yixin.forward(length)
    Yixin.left(120)
    Yixin.forward(length)

Yixin.color('blue')

def triangle(length, color1, color2, color3):
    Yixin.color(color1)
    Yixin.forward(length)
    Yixin.right(120)
    Yixin.color(color2)
    Yixin.forward(length)
    Yixin.right(120)
    Yixin.color(color3)
    Yixin.forward(length)

triangle(300, 'blue', 'green', 'yellow')

Yixin.color('green')
Yixin.begin_fill()
Yixin.forward(256)
Yixin.right(120)
Yixin.forward(256)
Yixin.right(120)
Yixin.forward(256)
Yixin.end_fill()

def square(length):
    Yixin.color('black')
    Yixin.forward(length)
    Yixin.left(90)
    Yixin.forward(length)
    Yixin.left(90)
    Yixin.forward(length)
    Yixin.left(90)
    Yixin.forward(length)
    Yixin.left(90)

square(50)
import random
Yixin.left(random.randint(45, 135))
Yixin.left(random.randint(45, 135))
square(80)
def fill_square():
    Yixin.begin_fill()
    square(100)
    Yixin.end_fill()

fill_square()
def fill_square(length):
    Yixin.left(random.randint(0, 360))
    Yixin.begin_fill()
    square(length)
    Yixin.end_fill()

fill_square(200)
Yixin.setposition(300, 300)
for times in range(360):
    Yixin.forward(5)
    Yixin.left(1)

Yixin.setposition(-200, -200)
def circle(arc_length, color):
    for times in range(360):
        Yixin.color(color)
        Yixin.forward(arc_length)
        Yixin.left(1)

circle(2, 'purple')