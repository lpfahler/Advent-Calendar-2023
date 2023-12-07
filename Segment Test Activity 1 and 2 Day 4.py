# Let it Glow Advent Calendar - Day 4
# Activities 1 and 2
# Lori Pfahler
# December 7, 2023

from machine import Pin
from utime import sleep

# Set up the LED pins
seg1 = Pin(13, Pin.OUT)
seg2 = Pin(12, Pin.OUT)
seg3 = Pin(11, Pin.OUT)
seg4 = Pin(10, Pin.OUT)
seg5 = Pin(9, Pin.OUT)

# Turn on each LED at a time
# make a list of the LED objects
seg_list = [seg1, seg2, seg3, seg4, seg5]
# use a for loop to turn on each of the segment LEDs
for LED in seg_list:
    LED.value(1)
    sleep(0.5)
# Turn all LEDs off
for LED in seg_list:
    LED.value(0)