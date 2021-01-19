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



window.exitonclick()
