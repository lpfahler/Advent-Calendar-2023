# Let it Glow Advent Calendar - Day 3
# Toggle Block (Red) LED and Internal LED (Green)
# Lori Pfahler
# December 5, 2023

from machine import Pin
from utime import sleep

# set up red and green buttons
redButton = Pin(20, Pin.IN, Pin.PULL_DOWN)
greenButton = Pin(21, Pin.IN, Pin.PULL_DOWN)

# setup block LED - red
blockLED = Pin(17, Pin.OUT)
# setup internal LED - green
internalLED = Pin(25, Pin.OUT)

# where the action happens
while True:
    sleep(0.2)
    if redButton.value() == 1:
        blockLED.toggle()
    if greenButton.value() == 1:
        internalLED.toggle()
        
