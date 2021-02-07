import turtle
import random

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

def make_turtle(shape):
    '''Makes a `Turtle` object

    Parameters:
    -----------
    shape: str.
        From the turtle documentation website, possible options are:
        'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
    penColor: str.
        Color string name (e.g. 'black', 'white', etc) that is to be the pen color of this turtle.

    Returns:
    -----------
    The `Turtle` object that you create.
    '''
    tur = turtle.Turtle()
    tur.speed(0)
    r = random.random()
    g = random.random()
    b = random.random()
    penColor = (r, g, b)
    tur.shape(shape)
    tur.begin_fill()
    tur.pencolor(penColor)
    tur.fillcolor(penColor)
    tur.end_fill()
    return tur

def goto(tur, angle, x, y):  
    '''
    Function setting turtle to position (x, y) with pen up and down
    '''
    tur.penup()
    tur.setheading(angle)
    tur.setposition(x, y)
    tur.pendown()

def reset_turtle(tur, screen_width, screen_height):
    '''
    Function resetting the turtle at the random positions of the edge of the screen
    ''' 
    penColor = [random.random() for _ in range(3)]
    tur.pencolor(penColor)
    tur.fillcolor(penColor)
    goto(tur, -90, random.randint(-screen_width/2, screen_width/2), screen_height/2) 

def move_and_stamp(tur, distance):
    '''
    Function moving and stamping turtle with specific distance
    '''
    tur.stamp()    
    tur.penup()
    tur.forward(distance)
    tur.pendown()

def writeNumStrides(tur, numStrides):
    '''
    Function writing out the times the function reset_turtle was called
    '''
    tur.clear()
    tur.write(numStrides, font=('Arial', 30, 'normal'))
    tur.hideturtle()


def main():

    screen = make_screen(500, 400,'Turtle Race', 'black')

    turt = make_turtle('turtle')
    arrow = make_turtle('arrow')
    circle = make_turtle('circle')

    writer = make_turtle('classic')
    writer.goto(0, -300)

    reset_turtle(turt, 500, 660)
    reset_turtle(arrow, 500, 660)
    reset_turtle(circle, 500, 660)

    # turtle_num('white')

    total = 0

    for times in range(1000):
        move_and_stamp(turt, 30) 
        move_and_stamp(arrow, 40) 
        move_and_stamp(circle, 50) 
        if turt.ycor() <= -330:
            reset_turtle(turt, 500, 660)
            total += 1
        if arrow.ycor() <= -330:
            reset_turtle(arrow, 500, 660)
            total += 1
        if circle.ycor() <= -330:
            reset_turtle(circle, 500, 660)
            total += 1
        # Method 1 write in every loop
        writeNumStrides(writer, total)
        



    screen.exitonclick()

    
if __name__ == '__main__':
    main()