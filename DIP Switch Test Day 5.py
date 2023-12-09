# Let it Glow Advent Calendar - Day 5
# DIP Switch ON Test
# Activities 1 and 2
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

# Try a different layout of results
print('Switch:')
print('1    2    3    4    5')

while True:    
    if dip1.value() == 1:
        condition1 = "ON "
    else:
        condition1 = "OFF"
        
    if dip2.value() == 1:
        condition2 = "ON "
    else:
        condition2 = "OFF"
        
    if dip3.value() == 1:
        condition3 = "ON "
    else:
        condition3 = "OFF"
        
    if dip4.value() == 1:
        condition4 = "ON "
    else:
        condition4 = "OFF"
    
    if dip5.value() == 1:
        condition5 = "ON "
    else:
        condition5 = "OFF"
    # use end parameter to replace this text rather than advancing the line in the shell    
    print(f'{condition1}  {condition2}  {condition3}  {condition4}  {condition5}', end = '\r')
    
    sleep(0.25) # delay
