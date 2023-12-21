# Let it Glow Advent Calendar - Day 11
# Secret Present List
# Lori Pfahler
# December 21, 2023

from utime import sleep
from machine import Pin
from neopixel import NeoPixel

# setup block LED - red
blockLED = Pin(21, Pin.OUT)

# Define the strand pin number (22) and number of LEDs (15)
strand = NeoPixel(Pin(22), 15)

# Color variables
off = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# LED index list
ledindex = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]

# Turn off all LEDs before program start
strand.fill((0,0,0))
strand.write()
sleep(1)

# Function with two arguments for colors
def blinky1(color1,color2):
    for led in ledindex:        
        if (led % 2) == 0: #If the LED index is even
            strand[led] = (color1)               
        else: # If not (odd numbers)
            strand[led] = (color2)        
        strand.write()

# Set up column pins on keypad
key1 = Pin(12, Pin.IN, Pin.PULL_DOWN)
key2 = Pin(13, Pin.IN, Pin.PULL_DOWN)
key3 = Pin(10, Pin.IN, Pin.PULL_DOWN)
key4 = Pin(11, Pin.IN, Pin.PULL_DOWN)

# Create list of presents
presents = ["Robot","3D Printer","Raspberry Pi 5","Lots of Candy!"]

# Set your passcode in a list
passcode = [1,2,3,4]

# Empty list for the entered password
userentry = []

# Create state variable
state = 0

# Create keypress variable
key = 0

# Append function
def appendkey():    
    global state
    userentry.append(key)
    print("*", end="")
    state = 1

# Delay + print function
def myprint(mytext):
    print(mytext)
    sleep(0.5)
    
## Start our program ##
print("") # Empty line
print("Welcome to the Secret Present List system")
sleep(1)
print("Enter the passcode to continue: ", end="")

# While userentry length is less than 4
while len(userentry) < 4:    
    sleep(0.1)    
    if state == 0:
        if key1.value() == 1:
            key = 1
            appendkey()
        elif key2.value() == 1:
            key = 2
            appendkey()           
        elif key3.value() == 1:
            key = 3
            appendkey()        
        elif key4.value() == 1:
            key = 4
            appendkey()
    
    # If state is 1 and all keys are LOW
    elif state == 1 and key1.value() == key2.value() == key3.value() == key4.value() == 0:        
        state = 0
        
    else:
        pass # Do nothing

# Program only gets this far if userentry is 4 characters long

# If the passcode is correct
if userentry == passcode:    
    blockLED.value(1) # LED on      
    blinky1(red, green)
    print("\n") #Empty newline
    print("----------------------")
    print("*** ACCESS GRANTED ***")
    myprint("----------------------")
    myprint("Secret present list:")
    
    # Print each present from our list
    for i in presents:
        myprint(i)

    myprint("----------------------")
    myprint("Happy Holidays and Thanks for Watching!")
    blockLED.value(0) # LED off
    blinky1(off, off)

# If the keyed code is incorrect
else:

    myprint("\n------------------")
    myprint("INCORRECT PASSCODE")
    myprint("ACCESS DENIED")
    sleep(1)