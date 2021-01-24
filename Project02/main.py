'''
Yixin Li
CS151 B
Project 2 - A Shape Collection
Jan 20, 2021
'''
'''The file works as the main code file for Project 2'''

import random
import turtle
screen = turtle.Screen()
t = turtle.Turtle()
import shapelib


def testScene():
    # shapelib.rectangle2(t, 0, 0, 1/4)
    # shapelib.rectangle2(t, 100, 50, 1)
    # shapelib.rectangle2(t, 200, 70, 2)
    # shapelib.rectangle2(t, 300, 100, 1/2)
    shapelib.triangle2(t, 0, 0, 1)
    shapelib.triangle2(t, 100, 100, 1/2)
    shapelib.triangle2(t, 200, -50, 1/3)
    shapelib.triangle2(t, 300, 200, 1/4)

# testScene()

screen.bgcolor('MidnightBlue')
t.speed(10)
def space1():
    for times in range(10):
        shapelib.meteor(t, random.randint(-300,300), random.randint(-300,300), 1/8, 'gold1')
    shapelib.rocket(t, -170, -150, 1/2, 'LightSkyBlue4')
    shapelib.rocket(t, -100, 150, 1/3, 'LightSkyBlue')
    shapelib.circle(t, 300, 300, 1/5, 'gold4')
    shapelib.circle(t, 250, 150, 1/4, 'DodgerBlue')
    shapelib.circle(t, 200, 250, 1/3, 'DeepSkyBlue2')
    shapelib.circle(t, 150, 100, 1/2, 'khaki')
    shapelib.circle(t, 70, 170, 1, 'LightSeaGreen')
    shapelib.circle(t, 40, 30, 1/4, 'firebrick4')
    shapelib.circle(t, -10, 100, 1/4, 'RoyalBlue')
    shapelib.circle(t, -50, 10, 1/5, 'tan')
    shapelib.circle(t, -100, -50, 1/4, 'chocolate')
    shapelib.circle(t, -300, -300, 2, 'yellow')
    shapelib.spaceship(t, 250, -250, 1)
    shapelib.spaceship(t, -250, 170, 1)
space1()


screen.exitonclick()