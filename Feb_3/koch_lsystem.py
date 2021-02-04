'''koch_lsystem.py
Draw a Koch snowflake using an L-system
'''

import turtle

''' Lindenmayer Systems '''
# IDEA Use characters in a string to tell turtle what to do
# Example: F means go forward, - means turn right, + means turn left
# Drawing a square: 'F+F+F+F+'

# L systems can be used to draw photo-realistic trees/plants
# It can be used to draw fractals
# It can be used to draw Koch snowflake

''' Koch Snowflake
Start with an initial shape:

Drawn with turtle, according to string
command = 'F--F--F'

What these symbols mean:
    F: turtle move forward a distance theta
    -: turtle turn left by theta degrees
    +: turtle turn right by theta degrees

Apply a replacement rule: Find 'F' in base string, replace it with 'F+F--F+F'

Replace 'F' with 'F+F--F+F'

So 'F--F--F' becomes 'F+F--F+F--F+F--F+F--F+F--F+F'

Let's implement an L-system to draw a Koch Snowflake
'''

def drawString(turt, string, distance, angle):
    '''Have `turt` draw the L-system string, where `turt` moves forward with a distance
    `distance` and turns at an angle `angle` degrees.

    Input:
        turt: turtle
        string: str, L-system command that turtle draws according to
        distance: int, distance of drawing forward
        angle: int, angle of one turn left or right
    Output:
        None
    '''

    for char in string:
        if char == 'F':
            turt.forward(distance)
        if char == '-':
            turt.left(angle)
        if char == '+':
            turt.right(angle)

def replace(string, findStr, repStr):
    '''Make a new string that applies the L-system replacement rules:
    Replace each occurence of `findStr` in `string` with `repStr`

    Input:
        string: str, the original string
        findStr: str, the part of string to be replaced
        repStr: str, another string to be replaced with
    Output:
        str, a new L-system command after all the replacement
    '''

    newString = ''
    for char in string:
        if char == findStr:
            newString = newString + repStr
        else:
            newString = newString + char

    return newString

if __name__ == '__main__':
    # Make a screen
    screen = turtle.Screen()
    screen.setup(600, 600)
    screen.tracer(False)

    # Make a turtle
    turt = turtle.Turtle()

    # Set up L-system rules
    baseStr = 'F--F--F'
    findStr = 'F'
    replaceStr = 'F+F--F+F'

    # Set up distance and angle for Koch snowflake
    distance = 3
    angle = 60

    # Apple the L-system replacement rules some number of times (iterations)
    numIterations = 5
    string = baseStr
    for i in range(numIterations):
        string = replace(string, findStr, replaceStr)

    # Draw the L-system
    drawString(turt, string, distance, angle)

    print(string)

    screen.update()
    screen.exitonclick()