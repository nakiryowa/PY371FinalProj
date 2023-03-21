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

def gw(pixels, threshold):
    """ Takes the 2-D list pixels containing pixels for an image, and 
        that creates and returns a new 2-D list of pixels for an image 
        that is a grey-and-white version of the original image.
        inputs: an integer threshold between 0 and 255 that should 
                govern which pixels are turned white and which are 
                turned grey.
    """
    gwimg = blank_image(len(pixels),len(pixels[0]))
    
    for r in range(len(pixels)):
        for c in range(len(pixels[0])):
            if brightness(pixels[r][c]) > threshold:
                gwimg[r][c] = [255,255,255]
            else:
                gwimg[r][c] = [128,128,128]
                
    return gwimg

# Everything above works. Below needs troubleshooting
# Taking out the below function for now as I don't think I need it
# def LEDdisplay(pixels):
    """ Creates a new image from the original, changing color values from 
        color to grey and white based on brightness, then converts it into
        a byte array for processing by an Arduino UNO.
    """              
    #pixels = gw(pixels, min(brightness(pixel)))
    
    #img = bytearray(pixels)
    
    #return img
