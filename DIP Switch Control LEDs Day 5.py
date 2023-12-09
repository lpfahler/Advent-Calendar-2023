# Let it Glow Advent Calendar - Day 5
# DIP Switch Control LED Bar Graph
# Activitiy 3
# Lori Pfahler
# December 9, 2023

from machine import Pin
import time

# Set up switch input pins
dip1 = Pin(2, Pin.IN, Pin.PULL_DOWN)
dip2 = Pin(3, Pin.IN, Pin.PULL_DOWN)
dip3 = Pin(4, Pin.IN, Pin.PULL_DOWN)
dip4 = Pin(5, Pin.IN, Pin.PULL_DOWN)
dip5 = Pin(6, Pin.IN, Pin.PULL_DOWN)

# Set up LED pins
seg5 = Pin(13, Pin.OUT)
seg4 = Pin(12, Pin.OUT)
seg3 = Pin(11, Pin.OUT)
seg2 = Pin(10, Pin.OUT)
seg1 = Pin(9, Pin.OUT)

while True:
    
    # Switch 1
    if dip1.value() == 1:
        seg1.value(1)
    else:
        seg1.value(0)

    # Switch 2
    if dip2.value() == 1:
        seg2.value(1)
    else:
        seg2.value(0)
        
    # Switch 3
    if dip3.value() == 1:
        seg3.value(1)
    else:
        seg3.value(0)

    # Switch 4
    if dip4.value() == 1:
        seg4.value(1)
    else:
        seg4.value(0)

    # Switch 5
    if dip5.value() == 1:
        seg5.value(1)
    else:
        seg5.value(0)
        
    # For each loop...
    time.sleep(0.5) # half second delay
