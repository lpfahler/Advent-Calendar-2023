# Let it Glow Advent Calendar - Day 12
# Send Greetings with associated lights using keypad
# Lori Pfahler
# December 23, 2023

from utime import sleep
from machine import Pin, I2C
from neopixel import NeoPixel
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

# Define the strand pin number (22) and number of LEDs (15)
strand = NeoPixel(Pin(22), 15)
strand.fill((0, 0, 0))
strand.write()
    

myColors ={
    'Red'   : (255,   0,   0), 
    'Green' : (  0, 255,   0), 
    'Blue'  : (  0,   0, 255), 
    'White' : (150, 150, 150),
    'Yellow': (255, 255,   0),
    'Purple': (255,   0, 150),
    'Pink'  : (200,  75,  80),
}

# Set up LCD I2C for LCD
lcdi2c = I2C(1, sda= Pin(14), scl=Pin(15), freq=400000)
lcd = I2cLcd(i2c = lcdi2c, i2c_addr = 0x27, num_lines = 2, num_columns = 16)

# Set up column pins on keypad
key1 = Pin(19, Pin.IN, Pin.PULL_DOWN)
key2 = Pin(18, Pin.IN, Pin.PULL_DOWN)
key3 = Pin(21, Pin.IN, Pin.PULL_DOWN)
key4 = Pin(20, Pin.IN, Pin.PULL_DOWN)

# variable to allow only one press on the keypad
state = 0

ledindex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

#  Two Colors on LED Strand
def twoColors(color1,color2):
    for led in ledindex:        
        if (led % 2) == 0: #If the LED index is even
            strand[led] = (color1)                
        else: # If not (odd numbers)
            strand[led] = (color2)        
    strand.write()

# variable to end the program
contProgram = True

while contProgram:    
    sleep(0.1) # Short delay    
    # If state = 0, allow checking for keypress
    if state == 0:    
        if key1.value() == 1:
            print("Button 1")
            lcd.clear()
            lcd.move_to(0, 0) # Move to first row
            lcd.putstr("Merry")            
            lcd.move_to(0, 1) # Move to second row
            lcd.putstr("Christmas!")
            state = 1
            twoColors(myColors['Red'], myColors['Green'])
        elif key2.value() == 1:
            print("Button 2")
            lcd.clear()
            lcd.move_to(0, 0) # Move to first row
            lcd.putstr("Happy")            
            lcd.move_to(0, 1) # Move to second row
            lcd.putstr("New Year!")
            state = 1
            twoColors(myColors['White'], myColors['Yellow'])          
        elif key3.value() == 1:
            print("Button 3")
            state = 1            
        elif key4.value() == 1:
            print("Button 4")
            state = 1
            lcd.clear()
            lcd.move_to(0, 0) # Move to first row
            lcd.putstr("Thanks for")
            lcd.move_to(0, 1) # Move to second row
            lcd.putstr("Watching!")
            twoColors(myColors['Purple'], myColors['Pink'])   
            sleep(5)
            endProgram = False
            lcd.clear()
            strand.fill((0, 0, 0))
            strand.write()

    # Only runs if state = 1 AND all keys are LOW
    elif state == 1 and key1.value() == key2.value() == key3.value() == key4.value() == 0:        
        state = 0
        
