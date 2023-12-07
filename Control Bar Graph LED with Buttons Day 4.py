# Let it Glow Advent Calendar - Day 4
# Control on Bar Graph LEDs with Buttons - Activity 5
# Lori Pfahler
# December 7, 2023

from machine import Pin
from utime import sleep

# Set up LED pins
seg1 = Pin(13, Pin.OUT)
seg2 = Pin(12, Pin.OUT)
seg3 = Pin(11, Pin.OUT)
seg4 = Pin(10, Pin.OUT)
seg5 = Pin(9, Pin.OUT)

# make a list of the LED objects
seg_list = [seg1, seg2, seg3, seg4, seg5]
# set up red and green buttons
redButton = Pin(20, Pin.IN, Pin.PULL_DOWN)
greenButton = Pin(21, Pin.IN, Pin.PULL_DOWN)
# Set the initial count for the index
count = -1

# use try and except to end program with <ctrl><c>
try: 
    while True:
        sleep(0.01)
        # if red button is pressed - turn on next LED
        if redButton.value() == 1:       
            if count == 4: 
                pass            
            else:
                count = count + 1 
                seg_list[count].on()
                sleep(0.2)
        # if green button is pressed - turn off next LED           
        if greenButton.value() == 1:       
            if count == -1: 
                pass            
            else:   
                seg_list[count].off() 
                sleep(0.2)
                count = count -1
except KeyboardInterrupt:
    # Turn all LEDs off
    for LED in seg_list:
        LED.value(0)