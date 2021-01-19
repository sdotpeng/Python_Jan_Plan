'''Create some additional functions that draw different shapes'''
'''Draw a clown'''

import turtle
window = turtle.Screen()
t = turtle.Turtle()


t.setposition(0,-200)
def face():
    t.pensize(4)
    t.pencolor('AntiqueWhite4')
    t.fillcolor('AntiqueWhite1')
    t.begin_fill()
    t.speed(1000)
    for times in range(360):
        t.forward(4)
        t.left(1)
    t.end_fill()
face()
t.penup()
t.setposition(-80,50)
t.pendown()

def eyes(r):
    t.pensize(4) 
    t.pencolor('CornFlowerBlue')
    t.fillcolor('white')
    t.begin_fill()
    t.speed(1000)     
    t.left(45)
    for loop in range(2):      
        t.circle(r,90)    
        t.circle(r/2,90)
    t.end_fill()
eyes(60)

t.penup()
t.setposition(-90,70)
t.setheading(0)
t.pendown()

def pupil(r):
    t.pensize(2) 
    t.pencolor('DodgerBlue4')
    t.fillcolor('DodgerBlue4')
    t.begin_fill()
    t.speed(1000)     
    t.left(45)
    for loop in range(2):      
        t.circle(r,90)    
        t.circle(r/2,90)
    t.end_fill()
pupil(30)

t.penup()
t.setposition(80,50)
t.seth(0)
t.pendown()
eyes(60)
t.penup()
t.setposition(75,70)
t.setheading(0)
t.pendown()
pupil(30)

t.penup()
t.setposition(-10,-10)
t.seth(0)
t.pendown()
def nose():
    t.pensize(3)
    t.pencolor('red4')
    t.fillcolor('red')
    t.begin_fill()
    t.speed(1000)
    for times in range(360):
        t.forward(0.5)
        t.left(1)
    t.end_fill()
nose()

t.penup()
t.setposition(0,-150)
t.seth(0)
t.pendown()
def mouth(color1, color2):
    t.pensize(3)
    t.pencolor(color1)
    t.fillcolor(color2)
    t.begin_fill()
    t.speed(1000)
    for times in range(360):
        t.forward(1)
        t.left(1)
    t.end_fill()
mouth('red4', 'red2')

t.penup()
t.setposition(0,-130)
t.seth(0)
t.pendown()
mouth('AntiqueWhite1','AntiqueWhite1')

t.penup()
t.setposition(-170,170)
t.seth(45)
t.pendown()
def hair1():
    t.pensize(40)
    t.pencolor('red2')
    t.fd(20)
    t.left(45)
    t.fd(20)
    t.right(45)
    t.fd(20)
    t.left(45)
    t.fd(20)
    t.right(60)
    t.fd(20)
hair1()

t.penup()
t.setposition(170,170)
t.seth(135)
t.pendown()
def hair2():
    t.pensize(40)
    t.pencolor('red2')
    t.fd(20)
    t.right(45)
    t.fd(20)
    t.left(45)
    t.fd(20)
    t.right(45)
    t.fd(20)
    t.left(60)
    t.fd(20)
hair2()

window.exitonclick()
