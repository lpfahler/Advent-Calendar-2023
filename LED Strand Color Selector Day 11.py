# Let it Glow Advent Calendar - Day 11
# LED Strand Color Selector
# Lori Pfahler
# December 21, 2023

from utime import sleep
from machine import Pin
from neopixel import NeoPixel

# Define the strand pin number (22) and number of LEDs (15)
strand = NeoPixel(Pin(22), 15)

# Set up column pins (inputs)
key1 = Pin(12, Pin.IN, Pin.PULL_DOWN)
key2 = Pin(13, Pin.IN, Pin.PULL_DOWN)
key3 = Pin(10, Pin.IN, Pin.PULL_DOWN)
key4 = Pin(11, Pin.IN, Pin.PULL_DOWN)

# Color variables
off = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)
purple = (255, 0, 255)

# LED index list
ledindex = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]

# Turn off all LEDs before program start
strand.fill((0,0,0))
strand.write()
sleep(1)

# Function with two arguments for colors
def blinky1(color1,color2):
    for led in ledindex:        
        if (led % 2) == 0: #If the LED index is even
            strand[led] = (color1)               
        else: # If not (odd numbers)
            strand[led] = (color2)        
        strand.write()

while True:    
    sleep(0.1)    
    if key1.value() == 1:        
        blinky1(red, green)        
    elif key2.value() == 1:      
        blinky1(white, blue)
    elif key3.value() == 1:        
        blinky1(yellow, purple)        
    elif key4.value() == 1:       
        blinky1(off, off)
