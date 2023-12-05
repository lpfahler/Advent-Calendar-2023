# Let it Glow Advent Calendar - Day 3
# Basic Button Usage - Activity 1
# Lori Pfahler
# December 5, 2023

from machine import Pin
from utime import sleep

# set up button
redButton = Pin(20, Pin.IN, Pin.PULL_DOWN)

# where the action happens
while True:
    sleep(0.2)
    if redButton.value() == 1:
        print('Red Button Pressed')