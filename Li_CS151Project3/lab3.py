'''
Yixin Li
CS151 B
Project 3 - Scenes Within Scenes
Jan 27, 2021
'''
import random
import turtle
import sys

def goto(t, x, y):  
    '''
    Function setting turtle to position (x, y) with pen up and down'''
    t.penup()
    t.setposition(x, y)
    t.setheading(0)
    t.pendown()

def rectangle(t, x, y, width, height):
    '''
    Draws a `width` x `height` rectangle with bottom-left corner positioned at (`x`, `y`).
    '''
    goto(t,x,y)
    for times in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)


def rectangle2(t, x, y, width, height, fill=False, edgeColor=(random.random(), random.random(), random.random()), fillColor=(random.random(), random.random(), random.random()), pensize=3): 
    '''
    Draws a `width` x `height` rectangle with bottom-left corner positioned at (`x`, `y`).
    The function also has keyword arguments for its color and pen size 
    '''
    t.color('black', (random.random(), random.random(), random.random()))
    t.pensize()
    if fill:
        t.begin_fill()
    rectangle(t, x, y, width, height)    
    if fill == True:
        t.end_fill()

def main(t, number):
    '''
    The main function of mondrian drawing
    '''
    for times in range(number):
        if random.random() < 0.4:
            t.begin_fill()
            rectangle2(t, random.randint(-500,500),random.randint(-500,500), random.randint(50,150), random.randint(50,150), fill=True, edgeColor=(random.random(), random.random(), random.random()), fillColor=(random.random(), random.random(), random.random()), pensize = 3)
            t.end_fill()
        else:
            rectangle2(t, random.randint(-500,500),random.randint(-500,500), random.randint(50,150), random.randint(50,150), fill=False, edgeColor=(random.random(), random.random(), random.random()), fillColor=(random.random(), random.random(), random.random()), pensize = 3)

if __name__== '__main__':

    window = turtle.Screen()
    t = turtle.Turtle()
    t.speed(10)
    main(t, 20)
    window.exitonclick()



