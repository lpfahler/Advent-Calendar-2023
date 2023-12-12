# Let it Glow Advent Calendar - Day 7
# Activity 3 - Slide Fader
# 
# Lori Pfahler
# December 13, 2023

from utime import sleep
from machine import Pin, ADC
from neopixel import NeoPixel

# Define GRBled1 pin number (22) and number of LEDs (1)
GRBled1 = NeoPixel(Pin(22), 1)
# Define GRBled2 pin number (21) and number of LEDs (1)
GRBled2 = NeoPixel(Pin(21), 1)

# Set up the slider on ADC pin 28
potentiometer = ADC(Pin(28))

try:
    while True:        
        # Read the potentiometer value
        potValue = potentiometer.read_u16() 
        
        # Take the analogue range (65535), divide it by the GRB range (255)
        # Then take the potentiometer reading and multiply it by that number
        # Round the number as our RGB code does not want floats
        GRBvalue = round(potValue * (255 / 65535))
        
        # Print the values using fstrings
        print(f'Potentiometer: {potValue:5d}, GRB Value: {GRBvalue:3d}', end= '\r')
         
        # Light the LEDs with the converted value
        GRBled1.fill((GRBvalue, 0, 0))
        GRBled1.write()
        GRBled2.fill((0, GRBvalue, 0))
        GRBled2.write()        
        sleep(0.1)

except KeyboardInterrupt:
    # turn LEDs off
    GRBled1.fill((0,0,0))
    GRBled1.write()
    GRBled2.fill((0,0,0))       
    GRBled2.write()