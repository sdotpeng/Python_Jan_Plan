# .jpg does compression
# does not represent lots of redudant info (pixels values all 0s in a sense)

''' solid_colors_sidebyside.py
Show to place two equally-sized images side-by-side in onw window
Siyuan Peng
TODO:
- On whiteboard, go over big picture: making a large canvas that fits 2 images.
- Write code below to make one 400x300 Image object then clone it - to ensure the same size
- Write the function to fill them in
- Make a larger canvas that would fit both Image objects side-by-side
- Display the canvas, hold until user clicks
- Write function to place the two images side-by-side
'''

import display
import graphics as gr

def solid_fill(img, r=0, g=0, b=0):
    '''Sets every pixel in the Image object `img` the RGB value (`r`, `b`, `g`)'''
    for y in range(img.getHeight()):
        for x in range(img.getWidth()):
            img.setPixel(x, y, gr.color_rgb(r, g, b))

def placeImageinCanvas(canvas, img, topleft_x, topleft_y):
    '''Place the image `img` into the larger canvas `canvas`. The image `img` should be
    positioned so that its top-left corner appears at (row, col) = (topleft_row, topleft_col)
    in the large canvas.
    NOTE: (0,0) is the top-left corner.

    Parameters:
    -----------
    canvas: Image. Larger canvas that fits two images side-by-side horizontally in a row
    img: Image. Image to be placed in one of the 2 slots on the canvas
    topleft_x: int. x pixel position (column) in `canvas` where the top-left corner of
                `img` should go
    topleft_y: int. y pixel position (row) in `canvas` where the top-left corner of
                `img` should go
    '''

    for y in range(img.getHeight()):
        for x in range(img.getWidth()):
            # Tuple unpacking
            (r, g, b) = img.getPixel(x, y)
            canvas.setPixel(x + topleft_x, y + topleft_y, gr.color_rgb(r, g, b))

if __name__ == '__main__':
    # Create a new 400x300 image (height x width format), then creating another by cloning
    # (deep copy)
    # Remember: Image constructor takes in width first, then height

    # my `red` image
    leftImg = gr.Image(gr.Point(0,0), 300, 400)

    # my `blue` image
    rightImg = leftImg.clone()

    # Fill the left and right images different solid colors
    solid_fill(leftImg, r=255)
    solid_fill(rightImg, b=255)

    # Make larger canvas that would fit both image horizontally side-by-side
    canvas = gr.Image(gr.Point(0,0), 2 * leftImg.getWidth(), leftImg.getHeight())

    # Place the images in a new window
    placeImageinCanvas(canvas, leftImg, 0, 0)
    placeImageinCanvas(canvas, rightImg, leftImg.getWidth(), 0)

    # Display the image in a new window
    screen = display.displayImage(canvas, 'Our canvas with two colors')

    # Display image until we get a mouse click
    screen.getMouse()
    screen.close()