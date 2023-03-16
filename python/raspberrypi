#
#
# PY371: Electronic Lab for Students
#
# Final Project: Moon Diagram
# Part I: Raspberry Pi - Python 3
#

from hmcpng import *
import RPi.GPIO as GPIO
import time
from gpiozero import LED
from gpiozero import PWMLED # for variable brightness; divide by 256

def create_uniform_image(height, width, pixel):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels have the RGB values
        given by pixel
        inputs: height and width are non-negative integers
                pixel is a 1-D list of RBG values of the form [R,G,B],
                     where each element is an integer between 0 and 255.
    """
    pixels = []

    for r in range(height):
        row = [pixel] * width
        pixels += [row]

    return pixels

def blank_image(height, width):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels are green.
        inputs: height and width are non-negative integers
    """
    all_green = create_uniform_image(height, width, [0, 255, 0])
    return all_green

def brightness(pixel):
    """ takes a pixel (an [R, G, B] list) and returns a value
        between 0 and 255 that represents the brightness of that pixel.
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    return (21*red + 72*green + 7*blue) // 100

def bw(pixels, threshold):
    """ Takes the 2-D list pixels containing pixels for an image, and 
        that creates and returns a new 2-D list of pixels for an image 
        that is a black-and-white version of the original image.
        inputs: an integer threshold between 0 and 255 that should 
                govern which pixels are turned white and which are 
                turned black.
    """
    bwimg = blank_image(len(pixels),len(pixels[0]))
    
    for r in range(len(pixels)):
        for c in range(len(pixels[0])):
            if brightness(pixels[r][c]) > threshold:
                bwimg[r][c] = [255,255,255]
            else:
                bwimg[r][c] = [0,0,0]
                
    return bwimg

def LEDdisplay(pixels):
    """ Creates a new image from the original, changing color values from 
        color to black and white based on brightness, then converts it into
        a byte array for processing by an Arduino UNO.
    """
    
    # leds = LEDBoard(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, \
                    #17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, \
                    #31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, \
                    #45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, \
                    #59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, \
                    #73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, \
                    #87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, \
                    #101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, \
                    #112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, \
                    #123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, \
                    #134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, \
                    #145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, \
                    #156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, \
                    #167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, \
                    #178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, \
                    #189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, \
                    #200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, \
                    #211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, \
                    #222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, \
                    #233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, \
                    #244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, \
                    #255, 256)
                    
    pixels = bw(pixels, min(brightness(pixel)))
    
    img = bytearray(pixels)
    
    return img
