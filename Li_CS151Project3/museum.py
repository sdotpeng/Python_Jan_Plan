'''
Yixin Li
CS151 B
Project 3 - Scenes Within Scenes
Jan 27, 2021
'''
# from Li_CS151Project3.better_shapelib import rectangle
import turtle
import random
import better_shapelib as bsl
import Extension2 as ex2


def mondrian_painting(t, scale, x_offset = 0, y_offset = 0):
    '''
    Function calling mondrian within a frame
    '''
    t.pencolor('Skyblue')
    t.pensize(8)
    bsl.rectangle(t, x_offset-100, y_offset-100, 250, 250)
    t.pensize(2)
    bsl.mondrian(t, 50, 100, 1 * scale, number = 80)

def space_painting(t, scale, x_offset = 0, y_offset = 0):
    '''
    Function calling a space scene within a frame
    '''
    t.pensize(6)
    t.pencolor('RoyalBlue4')
    bsl.rectangle(t, x_offset-150, y_offset-100, 200, 250)
    t.pensize(1)
    bsl.myScene(t, x_offset-80, y_offset, scale = 1/4)


def museum(t, scale, x_offset = 0, y_offset = 0):
    '''
    Function calling various painting scenes within museum scenes
    '''
    space_painting(t, x_offset = -200, y_offset = 0, scale = 1/8)
    mondrian_painting(t, 1/4)
    t.pensize(6)
    t.pencolor('gold4')
    bsl.rectangle(t, 230, 25, 220, 220)
    bsl.goto(t,350,120)
    ex2.star_painting(t,1)
    t.pensize(6)
    t.pencolor('peru')
    t.fillcolor('peru')
    t.begin_fill()
    bsl.rectangle(t, x_offset-500, y_offset-250, 1000, 50)
    t.end_fill()
    bsl.circle(t,x_offset-400, y_offset-300, 1/2, 'SandyBrown')
    bsl.circle(t,x_offset-250, y_offset-300, 1/2, 'SandyBrown')
    bsl.circle(t,x_offset-100, y_offset-300, 1/2, 'SandyBrown')
    bsl.circle(t,x_offset+50, y_offset-300, 1/2, 'SandyBrown')
    bsl.circle(t,x_offset+200, y_offset-300, 1/2, 'SandyBrown')
    bsl.circle(t,x_offset+350, y_offset-300, 1/2, 'SandyBrown')







if __name__== '__main__':
    window = turtle.Screen()
    t = turtle.Turtle()
    t.speed(10)
    window.bgcolor('LightGoldenRodYellow')
    museum(t, 1)
    window.exitonclick()
