# Why do we need loops?
# Because it saves time for a repeated task

# for <loop index> in range(<number of loop iterations>):
#   <loop body>

# range(number) returns an iterator
# for i in range(10):
#     print(i)

# for element in [1,3,5]:
#     print(element)

import turtle
window = turtle.Screen()
t = turtle.Turtle()

input('Press return to start...')

t.speed(1)
t.forward(300)
t.left(90)

t.speed(5)
t.forward(300)
t.left(90)

t.speed(10)
t.forward(300)
t.left(90)

t.speed(0)
t.forward(300)

for i in range(4):
    t.forward(300)
    t.left(90)

t.up()
t.setposition(-300,-300)
t.down()

for speed in [1,5,10,0]:
    t.speed(speed)
    t.forward(300)
    t.left(90)

for i in range(5):
    t.forward(200)
    t.left(72)

t.setposition(0, -300)
t.speed(10)

for num_side in range(4, 100):
    for i in range(num_side):
        t.forward(100)
        angle = (num_side - 2) * 180 / num_side
        t.left(180 - angle)

for i in range(500):
    t.forward(2)
    angle = (500 - 2) * 180 / 500
    t.left(180 - angle)

window.exitonclick()