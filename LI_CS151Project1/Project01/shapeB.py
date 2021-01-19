import turtle
window = turtle.Screen()
t = turtle.Turtle()

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



window.exitonclick()
