'''list_sidebyside.py
Use lists to organize imgae placement information
'''

import display
import graphics as gr
import solid_colors_sidebyside as solid

'''
-- Goal --
Orgranize the `Image` object and their placement information to easily control:
* where each of the two images go (left or right)
* what color to make them (red, blue, yellow, green, etc.)
* Can use list of lists to store information about each image in the canvas.
This information includes:
    * the x-coordinate of the top-left corner in the large canvas
    * the y-coordinate of the top-left corner in the large canvas
    * the solid color of the image
    * the `Image` object
'''

'''
Example: placing two images on the canvas
'''

# Use one sublist per image in the canvas (i.e. two sublists total)

# imageList = [
#     [0, 0, 'red', img], # Slot 1
#     [img.getWidth(), 0, 'blue', img] # Slot 2
# ]

# Coloring and placing images on the larger canvas
# Each sublist above contains all the information needed to color and lace an
# image in one of the canvas slots

# Loop through a list, deal with one sublist at a time, i.e. deal with one image at a time
# Clone the image object (blank image initially)
# "Paint" img the appropriate solid color, depending on the name in the sublist
# Place it on the canvas
# Display the canvas

def sideBySideList():
    '''
    Function to test out placing an image (left) next to its filtered version (right)
    '''

    # Create an image
    width = 300
    height = 400
    img = gr.Image(gr.Point(0, 0), width, height)

    # Make image list, with x, y placement info, how to process it (str),
    # and the `Image` object
    # We want a yellow image on the left, a pink one on the rights
    imgListofLists = [
        [0,0, 'pink', img],
        [width, 0, 'yellow', img]
    ]

    # Make 1x2 canvas
    canvas = gr.Image(gr.Point(0, 0), 2 * width, height)

    '''Process is:
    - Loop through the list, deal with one sublist at a time.
    - Clone the image object (original image by default).
    - Apply the solid color depending on the color name in the sublist.
    - Place it on the canvas.
    - Display.
    '''

    for imgList in imgListofLists: # imgList is a SUBLIST
        currentImage = imgList[-1].clone()

        if imgList[2] == 'red':
            solid.solid_fill(currentImage, r=255)
        elif imgList[2] == 'blue':
            solid.solid_fill(currentImage, b=255)
        elif imgList[2] == 'yellow':
            solid.solid_fill(currentImage, r=255, g=255)
        elif imgList[2] == 'pink':
            solid.solid_fill(currentImage, r=255, b=255)

        solid.placeImageinCanvas(canvas, currentImage, imgList[0], imgList[1])

        # Update image object in list of lists
        imgList[-1] = currentImage

    # Display canvas
    screen = display.displayImage(canvas, 'Our canvas')

    # Wait for mouse click to close window and end program
    screen.getMouse()

# main code
if __name__ == '__main__':
    sideBySideList()