# Let it Glow Advent Calendar - Day 5
# DIP Switch Choice of Program
# Activities 4 and 5 Sort of!
# Lori Pfahler
# December 9, 2023

from machine import Pin
from utime import sleep

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

# Create a list of our LEDs
seg_list = [seg1, seg2, seg3, seg4, seg5]

# Larson scanner function
def scanner():
    # Forwards through the list
    for LED in seg_list:        
        LED.on()
        sleep(0.05)
        LED.off()       
    # Backwards through the list
    for LED in reversed(seg_list):        
        LED.on()
        sleep(0.05)
        LED.off()
        
# Start Scan at Middle LED        
def middle_scan():
    # Out
    seg3.on()
    sleep(0.1)
    seg3.off()
    seg2.on()
    seg4.on()
    sleep(0.1)
    seg2.off()
    seg4.off()
    seg1.on()
    seg5.on()
    sleep(0.1)
    seg1.off()
    seg5.off()
    # In
    seg2.on()
    seg4.on()
    sleep(0.1)
    seg2.off()
    seg4.off()
    seg3.on()
    sleep(0.1)
    seg3.off()
    
while True:   
    # Switch 1
    if dip1.value() == 1:        
        print("Larson Scanner running...", end = '\r')
        scanner()

    # Switch 2
    elif dip2.value() == 1:        
        print("Middle Scan running...     ", end = '\r')
        middle_scan()
