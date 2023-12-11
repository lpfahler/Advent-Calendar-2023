# Let it Glow Advent Calendar - Day 6
# Cycle Colors Activity 3
# Added try and except to end program and turn off the LEDs
# Lori Pfahler
# December 11, 2023


# Imports
from utime import sleep
from machine import Pin
from neopixel import NeoPixel

# Define GRBled1 pin number (22) and number of LEDs (1)
GRBled1 = NeoPixel(Pin(22), 1)
# Define GRBled2 pin number (21) and number of LEDs (1)
GRBled2 = NeoPixel(Pin(21), 1)

# Define some GRB color variables
white = (240, 140, 255) 
red = (0, 255, 0)
green = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 175, 150)
orange = (238, 223, 105)
pink = (150, 150, 200)
purple = (40, 100, 255)
iceblue = (150, 25, 200)
unicorn = (175, 150, 255)
bogey = (215, 100, 0)

# Define our colour list
colors = [white, red, green, blue, yellow, orange, pink, purple, iceblue, unicorn, bogey]

try: 
    while True:
        # loop through the colors list
        for color in colors:       
            GRBled1.fill((color))    
            GRBled1.write()
            GRBled2.fill((color))    
            GRBled2.write()  
            sleep(0.2)
            
except KeyboardInterrupt:
    # turn them off
    GRBled1.fill((0,0,0))
    GRBled1.write()
    GRBled2.fill((0,0,0))       
    GRBled2.write()    