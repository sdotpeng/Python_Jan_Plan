import turtle
import random

def make_screen(width, height, title, color):
    '''
    Makes a 'screen' object
    '''
    screen = turtle.Screen()
    screen.window_width == width
    screen.window_height == height
    screen.title(title)
    screen.bgcolor(color)
    
    return screen

def make_turtle(shape):
    '''
    Makes a 'Turtle' object
    '''
    tur = turtle.Turtle()
    tur.speed(10)
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

def stampI(tur, distance):
    '''
    Function moving and stamping turtle with specific distance
    '''
    tur.clear()
    tur.stamp()  
    tur.write('I', font=('Times', 30, 'normal'))
    tur.hideturtle() 
    tur.penup()
    tur.forward(distance)
    tur.pendown()

def stampM(tur, distance): 
    '''
    Function moving and stamping turtle with specific distance
    '''  
    tur.clear()
    tur.stamp()  
    tur.write('M', font=('Times', 30, 'normal'))
    tur.hideturtle() 
    tur.penup()
    tur.forward(distance)
    tur.pendown()

def stampi(tur, distance):   
    '''
    Function moving and stamping turtle with specific distance
    '''
    tur.clear()
    tur.stamp()  
    tur.write('i', font=('Times', 30, 'normal'))
    tur.hideturtle() 
    tur.penup()
    tur.forward(distance)
    tur.pendown()

def stamps(tur, distance):
    '''
    Function moving and stamping turtle with specific distance
    '''
    tur.clear()   
    tur.stamp()  
    tur.write('s', font=('Times', 30, 'normal'))
    tur.hideturtle() 
    tur.penup()
    tur.forward(distance)
    tur.pendown()

def stampY(tur, distance):
    '''
    Function moving and stamping turtle with specific distance
    '''
    tur.clear()
    tur.stamp()  
    tur.write('Y', font=('Times', 30, 'normal'))
    tur.hideturtle() 
    tur.penup()
    tur.forward(distance)
    tur.pendown()

def stampo(tur, distance):
    '''
    Function moving and stamping turtle with specific distance
    '''
    tur.clear()
    tur.stamp()  
    tur.write('o', font=('Times', 30, 'normal'))
    tur.hideturtle() 
    tur.penup()
    tur.forward(distance)
    tur.pendown()

def stampu(tur, distance):
    '''
    Function moving and stamping turtle with specific distance
    '''
    tur.clear()
    tur.stamp()  
    tur.write('u', font=('Times', 30, 'normal'))
    tur.hideturtle() 
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

    screen = make_screen(500, 400,'Mystery', 'black')

    turt = make_turtle('classic')
    turt1 = make_turtle('classic')
    turt2 = make_turtle('classic')
    turt3 = make_turtle('classic')
    turt4 = make_turtle('classic')
    turt5 = make_turtle('classic')
    turt6 = make_turtle('classic')
    turt7 = make_turtle('classic')

   
    reset_turtle(turt, 500, 660)
    reset_turtle(turt1, 500, 660)
    reset_turtle(turt2, 500, 660)
    reset_turtle(turt3, 500, 660)
    reset_turtle(turt4, 500, 660)
    reset_turtle(turt5, 500, 660)
    reset_turtle(turt6, 500, 660)
    reset_turtle(turt7, 500, 660)
  

    total = 0

    for times in range(99):
        stampI(turt, 60)  
        stampM(turt1, 80)
        stampi(turt2, 50)
        stamps(turt3, 40)
        stamps(turt4, 40)
        stampY(turt5, 70)
        stampo(turt6, 60)
        stampu(turt7, 50)


        if turt.ycor() <= -330:
            reset_turtle(turt, 500, 660)
        if turt1.ycor() <= -330:
            reset_turtle(turt1, 500, 660)
        if turt2.ycor() <= -330:
            reset_turtle(turt2, 500, 660)
        if turt3.ycor() <= -330:
            reset_turtle(turt3, 500, 660)
        if turt4.ycor() <= -330:
            reset_turtle(turt4, 500, 660)
        if turt5.ycor() <= -330:
            reset_turtle(turt5, 500, 660)
        if turt6.ycor() <= -330:
            reset_turtle(turt6, 500, 660)        
        if turt7.ycor() <= -330:
            reset_turtle(turt7, 500, 660)


    screen.exitonclick()

    
if __name__ == '__main__':
    main()