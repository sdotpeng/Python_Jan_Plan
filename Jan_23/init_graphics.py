# Zelle Graphics
import graphics as gr

# In Turtle, we create a screen by the following line
# screen = turtle.Screen()

# In Graphics, we use GraphWin()
screen = gr.GraphWin("Ricky is drawing", width=500, height=400)

# In Turtle, we use screen.exitonclick() to exit
# In Graphics, we use screen.getMouse() to pause and wait for a click
# And, we use screen.close() to exit

screen.getMouse()
# screen.close()

# In Graphics module, we can create different types of object, including:
# Point, Line, Rectangle, Circle, Oval, Polygon, Image

# Point(x, y): x and y are the coordinates of the point
P1 = gr.Point(100, 100)
P2 = gr.Point(300, 300)

# obj.draw(graphWin): graphWin is the screen we defined
# The following are invalid
# draw(P1), P1.draw()
# draw(): Actually draws the object you create in the window
# NOTE: Creating an object does not mean it shows up in the window! You need to run its draw function
P1.draw(screen)
P2.draw(screen)

# Rectangle(Point1, Point2): Point1, Point2 are the top left and buttom right points of the rectangle
Rec = gr.Rectangle(P1, P2)
Rec.draw(screen)

# Circle(Point, radius): Point is the centre of the circle, and radius is a integer
C = gr.Circle(P1, 50)
C.draw(screen)

screen.getMouse()

# undraw(): Removes a drawn shape from the canvas
C.undraw()

# move(dx, dy): Move the object in the window horizontally by dx, vertically by dy
C.move(50, 50)

# setOutline(color): Sets the outline edge of the shape to color, e.g. a named string like
# red or in graphics.color_rgb(r,g,b) format
C.setOutline('red')

# graphics.color_rgb() will return a string
color1 = gr.color_rgb(155,155,155)
C.setOutline(color1)

# setWidth(width): Sets the width of the outline edge, in pixels
C.setWidth(10)

# setFill(color): Sets the interior surface color, e.g. a named string like 'red' or
# in graphics.color_rgb(r,g,b) format
C.setFill('pink')

# NOTE: We use getCenter() to return a gr.Point object from a circle object
# NOTE: We use getP1() and getP2() to return two points from gr.Rectangle() object
center = C.getCenter()
# NOTE: We use getX() and getY() to return the x and y coordinate of a gr.Point object
center.getX()

screen.getMouse()
screen.close()
