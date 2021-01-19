'''Draw an n-gon'''

import turtle
window = turtle.Screen()
t = turtle.Turtle()

def n_gon(side_length, num_side):
    angle = 360 / num_side
    for i in range(num_side):
        t.forward(side_length)
        t.right(angle)
n_gon(60, 18)
n_gon(30,5)
n_gon(40,12)
n_gon(20,6)

window.exitonclick()