import  turtle
import random
import lab04 as l4
import object_shapelib as os

def make_turtle(shape, penColor):
    '''
    Function making a `Turtle` object copied from lab04
    '''
    tur = turtle.Turtle()
    tur.speed(10)
    r = random.random()
    g = random.random()
    b = random.random()
    tur.shape(shape)
    tur.begin_fill()
    tur.pencolor(penColor)
    tur.fillcolor(penColor)
    tur.end_fill()
    return tur

def move_turtle(turt1, turt2, turt3, turt4, angle, radius, extent):
    '''
    Moves the `Turtle` object `turt` `speed` units
    '''
    for times in range(angle):
        turt1.circle(radius = 180, extent = 360 / int(angle))
        turt2.circle(radius = 160, extent = 180 / int(angle))
        turt3.circle(radius = 140, extent = 120/ int(angle))
        turt4.circle(radius = 125, extent = 100/ int(angle))




def main(turt):
    '''
    Function combining race track, race scene, and turtles together
    '''
    l4.make_screen(500, 400, 'Turtle Race', 'ForestGreen') 
    os.draw_race_scene(turt)
    l4.goto(rt1, 180, 0, 220)
    l4.goto(rt2, 180, 0, 200)
    l4.goto(rt3, 180, 0, 180)
    l4.goto(rt4, 180, 0, 160)
    l4.goto(sk1, 90, 50, 260)
    l4.goto(sk2, 90, 70, 260)
    l4.goto(sk3, 90, 90, 260)
    l4.goto(sk4, 90, 110, 260)

if __name__ == '__main__':

    rt1 = make_turtle('turtle', 'DeepSkyBlue2')
    rt2 = make_turtle('classic', 'hotpink')
    rt3 = make_turtle('triangle', 'LightGreen')
    rt4 = make_turtle('square', 'LightBlue')
    sk1 = make_turtle('arrow', 'DodgerBlue')
    sk2 = make_turtle('arrow', 'LightCoral')
    sk3 = make_turtle('arrow', 'OliveDrab1')
    sk4 = make_turtle('arrow', 'SteelBlue2')

    screen = turtle.Screen()
    turt = turtle.Turtle()
    total1 = 0
    total2 = 0
    total3 = 0
    total4 = 0

    main(turt)
    for times in range(1000):
        move_turtle(rt1, rt2, rt3, rt4, random.randint(20,180), 180, 160)
        if rt1.xcor() >= -10 and rt1.xcor() <= 10:
            if rt1.ycor() >= 0:
                total1 += 1
        if rt2.xcor() >= -10 and rt2.xcor() <= 10:
            if rt2.ycor() >= 0:
                total2 += 1
        if rt3.xcor() >= -10 and rt3.xcor() <= 10:
            if rt3.ycor() >= 0:
                total3 += 1
        if rt4.xcor() >= -10 and rt4.xcor() <= 10:
            if rt4.ycor() >= 0:
                total4 += 1
        l4.writeNumStrides(sk1, total1)
        l4.writeNumStrides(sk2, total2)
        l4.writeNumStrides(sk3, total3)
        l4.writeNumStrides(sk4, total4)

    screen.exitonclick()