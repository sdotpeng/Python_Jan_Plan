# When we defined some functions these days, we pass none or several parameters to them
# Up to now, these are all called positional arguments.

# Parameters in a Python functions have two types, positional arguments and keyword arguments.

def morning_routine(breakfast_choice, dress_choice):
    print('Breakfast Choice:', breakfast_choice)
    print('Dress Choice:', dress_choice)

morning_routine('chinese', 'work')
morning_routine('work', 'chinese')

def morning_routine2(breakfast_choice='chinese', dress_choice='work'):
    print('Breakfast Choice:', breakfast_choice)
    print('Dress Choice:', dress_choice)

morning_routine2(breakfast_choice='american', dress_choice='casual')
morning_routine2(dress_choice='formal', breakfast_choice='indian')


morning_routine2()

import turtle
window = turtle.Screen()
t = turtle.Turtle()

input("Press return to proceed...")

def circle(length, color='yellow'):
    t.color(color)
    t.circle(length)

circle(50)
circle(80, color='red')

# The following two lines will result in errors Why?
circle(color='red')
circle(100, color='green')

window.exitonclick()