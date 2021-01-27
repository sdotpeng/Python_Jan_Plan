import graphics as gr
import display

# Load image
img = gr.Image(gr.Point(200, 200), 'Jan_26/miller.ppm')
print(type(img))

# Show screen
screen = display.displayImage(img, 'This is Miller Library!')

# Close screen
screen.getMouse()
screen.close()