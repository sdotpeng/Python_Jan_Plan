import turtle
import random
import lab04 as l4
screen = turtle.Screen()
turt = turtle.Turtle()

def make_screen(width, height, title, color):
    '''Makes a `Screen` object: the window in each turtles can draw shapes

    Parameters:
    -----------
    width: int.
        The width of the window/screen in pixels.
    height: int.
        The height of the window/screen in pixels.
    title: str.
        The name that you'd like to call the pop-up window. Appears at the center of top of the window.
    color: str.
        Color string name (e.g. 'black', 'white', etc). This is the background color of the screen.

    Returns:
    -----------
    The `Screen` object that you create.
    '''
    screen = turtle.Screen()
    screen.window_width == width
    screen.window_height == height
    screen.title(title)
    screen.bgcolor(color)
    
    return screen

def goto(turt, x, y, heading=0):
    '''
    Function setting turtle to position (x, y) with pen up and down
    '''
    turt.penup()
    turt.setheading(heading)
    turt.setposition(x, y)
    turt.pendown() 

def circle(turt, x, y, arc_length, penWidth=5, penColor = 'white', fillColor='brown'):
    '''
    Function making a circular race track for turtles
    '''
    goto(turt, x, y)
    turt.speed(10)
    turt.pencolor(penColor)
    turt.pensize(penWidth)
    turt.fillcolor(fillColor)
    turt.begin_fill()
    for times in range(360):
        turt.forward(arc_length)
        turt.left(1)
    turt.end_fill()

def tree(turt, x, y):
    '''
    Function drawing trees with position (x, y)
    '''
    turt.speed(10)
    turt.pensize(3)
    turt.fillcolor('sienna')
    turt.pencolor('sienna4')
    goto(turt,x+10,y)
    turt.begin_fill()
    turt.right(90)
    turt.fd(90)
    turt.right(90)
    turt.fd(20)
    turt.right(90)
    turt.fd(90)
    turt.right(90)
    turt.fd(20)
    turt.end_fill()
    goto(turt, x, y, heading = 90)
    turt.pencolor('SpringGreen4')
    turt.pensize(3)
    turt.fillcolor('LimeGreen')
    turt.begin_fill()
    circle(turt, x, y, 0.8, penWidth=5, penColor='DarkGreen', fillColor='LimeGreen')
    turt.end_fill()

def flag(turt,x,y):
    '''
    Function drawing a flag
    '''
    turt.speed(10)
    turt.pensize(3)
    turt.fillcolor('gold1')
    turt.pencolor('gold4')
    goto(turt, x, y, heading=90)
    turt.begin_fill()
    turt.fd(90)
    turt.right(90)
    turt.fd(50)
    turt.right(135)
    turt.fd(40)
    turt.left(90)
    turt.fd(40)
    turt.right(135)
    turt.fd(50)
    turt.end_fill()

def draw_race_scene(turt):
    '''
    Function drawing the turtle race track
    '''
    circle(turt, 0, -200, 4)
    circle(turt, 0, -78, 2, fillColor = 'ForestGreen')
    flag(turt, 0, 230)
    tree(turt, 250, 220)
    tree(turt, 300, 210)
    tree(turt, 220, 200)
    tree(turt, 280, 0)
    tree(turt, 300, -120)
    tree(turt, -200, -150)
    tree(turt, 250, -170)
    tree(turt, 140, -250)

if __name__ == '__main__':
    make_screen(500, 400, 'Turtle Race', 'ForestGreen')
    draw_race_scene(turt)
    
    
    screen.exitonclick()
