
import turtle
import random


def goto(t, x, y):
    '''Sets turtle to position (x, y) with pen up and pen down'''
    print(t)
    t.penup()
    t.setposition(x, y)
    t.setheading(0)
    t.pendown()


def rectangle(t, x, y, width, height):
    '''Draws a `width` x `height` rectangle with bottom-left corner positioned at (`x`, `y`).
    '''
    goto(t,x,y)
    for times in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

def rectangle2(t, x, y, width, height, fill=False, edgeColor=(random.random(), random.random(), random.random()), fillColor=(random.random(), random.random(), random.random()), pensize=3): 
    '''Draws a rectangle with random edge and pen colors'''
    t.color('black', (random.random(), random.random(), random.random()))
    t.pensize()
    if fill:
        t.begin_fill()
    rectangle(t, x, y, width, height)
    if fill == True:
        t.end_fill()

def mondrian(t, x, y, s, number):
    '''Draws mondrian with specific scale and rectangle number'''
    goto(t, x, y)
    for times in range(number):
        if random.random() < 0.4:
            t.begin_fill()
            rectangle2(t, random.randint(-100,100), random.randint(-100,100), random.randint(50,150) * s, random.randint(50,150) * s, fill=True, edgeColor=(random.random(), random.random(), random.random()), fillColor=(random.random(), random.random(), random.random()), pensize = 3)
            t.end_fill()
        else:
            rectangle2(t, random.randint(-100,100), random.randint(-100,100), random.randint(50,150) * s, random.randint(50,150) * s, fill=False, edgeColor=(random.random(), random.random(), random.random()), fillColor=(random.random(), random.random(), random.random()), pensize = 3)


def star(t, x, y, scale, color, fill=False): 
    '''Function of creating a star shape: the 1st simple shape copied'''
    goto(t, x, y)
    t.fillcolor(color)
    if fill:
        t.begin_fill()
    for times in range(5):
        t.forward(100 * scale)
        t.right(144)
    if fill == True:
        t.end_fill()


def triangle(t, x, y, scale, color, fill=False): 
    '''Function of creating a triangle shape: the 2nd simple shape copied'''
    goto(t, x, y)
    t.fillcolor(color)
    if fill:
        t.begin_fill()
    for times in range(3):
        t.forward(100*scale)
        t.left(120)
    if fill == True:
        t.end_fill()

def triangleStack(t, x, y, scale, fill = False): 
    '''Function drawing three triangles on top of each other: the 1st compound shape copied'''
    goto(t, x, y)
    t.fillcolor()
    if fill:
        t.begin_fill()
    triangle(t, x, y, scale * 2, color=(random.random(), random.random(), random.random()))
    t.end_fill()
    t.begin_fill()
    triangle(t, x + scale * 50, y + scale * 173.2, scale * 1, color=(random.random(), random.random(), random.random()))
    t.end_fill()
    t.begin_fill()
    triangle(t, x + scale * 75, y + scale * 259.81, scale * 0.5, color=(random.random(), random.random(), random.random()))
    if fill == True:
        t.end_fill()

def meteor(t, x, y, scale, color, fill = False):
    '''Function of creating meteor: the 2nd compound shape copied'''
    goto(t, x, y)
    t.fillcolor(color)
    t.begin_fill()
    star(t, x, y, scale * 2, color)
    star(t, x + scale * 200, y + scale * 0, scale * 1, color)
    star(t, x + scale * 300, y + scale * 0, scale * 0.5, color)
    rectangle2(t, x + scale * 350, y + scale * 0, scale * 1/3, scale*1/2)
    t.end_fill()

def rocket(t, x, y, scale, color):
    '''Function of creating rocket: the simple shape created for scene'''
    goto(t, x, y)
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    triangle(t, x, y, scale * 1, color)
    triangle(t, x + scale * 25, y + scale * 86.61, scale * 0.5, color)
    rectangle(t, x + scale * 0, y + scale * 0, scale * 1, scale * 2)
    star(t, x + scale * 0, y + scale * -238.2, scale * 1, color)
    t.end_fill()

def circle(t, x, y, arc_length, color):
    '''Function defining a circle with fill color'''
    goto(t, x, y)
    t.speed(10)
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    for times in range(360):
        t.forward(arc_length)
        t.left(1)
    t.end_fill()


def myScene(t, x_offset = 0, y_offset = 0, scale = 1):
    '''Function of my scene'''
    rocket(t, x_offset-170 * scale, y_offset-150 * scale, 1/2 * scale, 'LightSkyBlue4')
    rocket(t, x_offset-100 * scale, y_offset+150 * scale, 1/3 * scale, 'LightSkyBlue')
    circle(t, x_offset+300 * scale, y_offset+300 * scale, 1/5 * scale, 'gold4')
    circle(t, x_offset+250 * scale, y_offset+150 * scale, 1/4 * scale, 'DodgerBlue')
    circle(t, x_offset+200 * scale, y_offset+250 * scale, 1/3 * scale, 'DeepSkyBlue2')
    circle(t, x_offset+150 * scale, y_offset+100 * scale, 1/2 * scale, 'khaki')
    circle(t, x_offset+70 * scale, y_offset+170 * scale, 1 * scale, 'LightSeaGreen')
    circle(t, x_offset+40 * scale, y_offset+30 * scale, 1/4 * scale, 'firebrick4')
    circle(t, x_offset-10 * scale, y_offset+100 * scale, 1/4 * scale, 'RoyalBlue')
    circle(t, x_offset-50 * scale, y_offset+10 * scale, 1/5 * scale, 'tan')
    circle(t, x_offset-100 * scale, y_offset-50 * scale, 1/4 * scale, 'chocolate')


# if __name__== '__main__':
#     window = turtle.Screen()
#     t = turtle.Turtle()
#     t.speed(10)
#     window.bgcolor('MidnightBlue')
#     # meteor(t, random.randint(-300,300), random.randint(-300,300), 1/7, 'red')
#     myScene(t,0,0,1/2)
#     myScene(t, -300, -300, 1/3)
#     myScene(t, 300, 300, 1/4)

    # window.exitonclick()
