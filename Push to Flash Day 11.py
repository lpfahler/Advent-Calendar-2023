# Let it Glow Advent Calendar - Day 11
# Push to Flash
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

# setup block LED - red
blockLED = Pin(21, Pin.OUT)

# Create our simple function
def flashLED(flash):
    blockLED.on() # LED ON
    strand.fill((100, 0, 0)) # led strand on        
    strand.write()
    sleep(flash)   
    blockLED.off() # LED off
    strand.fill((0, 0, 0))  # led strand off      
    strand.write()
    sleep(flash)
        
while True:
    # "listen" for button presses
    while key1.value() == 1:
        flashLED(0.5)
    while key2.value() == 1:
        flashLED(0.25)
    while key3.value() == 1:
        flashLED(0.1)
    while key4.value() == 1:
        flashLED(0.05)

