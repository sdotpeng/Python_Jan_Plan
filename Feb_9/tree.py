''' tree.py
Uses recursion and turtle to draw tree
'''

import turtle

class Tree:
    def __init__(self, start_x, start_y):
        '''
        Get turtle ready and in-position to draw an upright tree.
        Show animations (but fast ones) with speed of 7
        '''
        self.screen = turtle.Screen()
        self.turt = turtle.Turtle()
        self.turt.setheading(90)
        self.turt.speed(7)
        self.turt.color('purple')
        self.goto(start_x, start_y)

    def goto(self, x, y):
        self.turt.penup()
        self.turt.goto(x, y)
        self.turt.pendown()

    def hold(self):
        self.screen.exitonclick()

    def drawTree(self, distance):
        ''' Draw a tree recursively with initial trunk/branch length `distance`.
            - Draw branches that look like 'forks': straight part then left and rigght offshots
                +/- deg offset from straight
            - Stop drawing branches when the branch distance is <= 5
            - After drawing left, right, and straight portions, always restore the turtle position
                to what it was before drawing the 'fork'
        '''

        if distance <= 5:
            return

        # Draw `straight ahead` trunk
        self.turt.forward(distance)

        # Before drawing left branch, save position so we know where to go back to
        # when going to draw their right branch
        x, y = self.turt.position()
        head = self.turt.heading()

        # Draw left branch
        self.turt.left(20)
        self.drawTree(distance/2) # took care of left branch

        # Get ready for right branch
        self.turt.setheading(head)
        self.turt.right(20)
        self.turt.setpos(x, y)

        # Draw right branch
        self.drawTree(distance/2)

        # Restore turtle to before drawing right branch
        self.turt.left(20) # Facing north again
        self.turt.setpos(x, y)

if __name__ == '__main__':
    tree = Tree(0, -400)
    tree.drawTree(250)
    tree.hold()
