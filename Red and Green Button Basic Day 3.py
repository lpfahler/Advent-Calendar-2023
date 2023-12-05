# Let it Glow Advent Calendar - Day 3
# Multiple Button Inputs, Red and Green Buttons - Activity 2
# Lori Pfahler
# December 5, 2023

from machine import Pin
from utime import sleep

# set up red and green buttons
redButton = Pin(20, Pin.IN, Pin.PULL_DOWN)
greenButton = Pin(21, Pin.IN, Pin.PULL_DOWN)

# where the action happens
while True:
    sleep(0.2)
    if redButton.value() == 1:
        print('Red Button Pressed')
    if greenButton.value() == 1:
        print('Green Button Pressed')
