import random
import display
import graphics as gr

'''
Create a Zelle Image with random RGB values
'''

# Set random RGB value on every pixel
# for x in range(width):
#     for y in range(height):
#         r = random.randint(0, 255)
#         g = random.randint(0, 255)
#         b = random.randint(0, 255)
#         img.setPixel(x, y, gr.color_rgb(r, g, b))

def set_random_RGB(img):
    ''' Set random RGB values on each pixel of the given image
    Input:
        img: graphics.Image object
    Return:
        None
    '''
    for x in range(img.getHeight()):
        for y in range(img.getWidth()):
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            img.setPixel(x, y, gr.color_rgb(r, g, b))

if __name__ == '__main__':

    width = 800
    height = 600

    # Create an empty Image object
    img = gr.Image(gr.Point(0,0), width, height)

    # Call the function
    set_random_RGB(img)

    screen = display.displayImage(img, 'Our rainbow image!')

    screen.getMouse()
    screen.close()

