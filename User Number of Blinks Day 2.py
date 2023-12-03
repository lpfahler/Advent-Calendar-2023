# Let it Glow Advent Calendar - Day 2
# User Choice for Number of Blinks - Activity 5 Sort of!
# Lori Pfahler
# December 3, 2023

from machine import Pin
from utime import sleep

# setup block LED - red
blockLED = Pin(17, Pin.OUT)

# ask user for number of blinks
# turn string from input function into an integer
nBlinks = int(input('Enter number of blinks: '))

# blink LED user number of times
for i in range(nBlinks):
    blockLED.on()
    sleep(0.5)
    blockLED.off()
    sleep(0.5)

