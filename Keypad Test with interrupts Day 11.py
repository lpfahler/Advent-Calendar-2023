# Let it Glow Advent Calendar - Day 11
# Basic Keypad Test
# Lori Pfahler
# December 21, 2023

from utime import sleep, ticks_ms, ticks_diff
from machine import Pin, ADC
from neopixel import NeoPixel

# Define the strand pin number (22) and number of LEDs (15)
strand = NeoPixel(Pin(22), 15)


# Set up column pins (inputs)
key1 = Pin(12, Pin.IN, Pin.PULL_DOWN)
key2 = Pin(13, Pin.IN, Pin.PULL_DOWN)
key3 = Pin(10, Pin.IN, Pin.PULL_DOWN)
key4 = Pin(11, Pin.IN, Pin.PULL_DOWN)

# variables to track interrupt activation and time for debouncing
key1_debounce_time = ticks_ms()
key2_debounce_time = ticks_ms()
key3_debounce_time = ticks_ms()
key4_debounce_time = ticks_ms()
key1_flag = 0
key2_flag = 0
key3_flag = 0
key4_flag = 0

# interrupt function for key1 button
def key1_handler(key1):
    global key1_debounce_time, key1_flag
    if ticks_diff(ticks_ms(), key1_debounce_time) > 1000:
        key1_flag = 1
        # print('key1_flag:', key1_flag)
        key1_debounce_time = ticks_ms()

# interrupt function for key2 button
def key2_handler(key2):
    global key2_debounce_time, key2_flag
    if ticks_diff(ticks_ms(), key2_debounce_time) > 1000:
        key2_flag = 1
        # print('key2_flag:', key2_flag)
        key2_debounce_time = ticks_ms()

# interrupt function for key3 button
def key3_handler(key3):
    global key3_debounce_time, key3_flag
    if ticks_diff(ticks_ms(), key3_debounce_time) > 1000:
        key3_flag = 1
        # print('key3_flag:', key3_flag)
        key3_debounce_time = ticks_ms()

# interrupt function for key4 button
def key4_handler(key4):
    global key4_debounce_time, key4_flag
    if ticks_diff(ticks_ms(), key4_debounce_time) > 1000:
        key4_flag = 1
        # print('key4_flag:', key4_flag)
        key4_debounce_time = ticks_ms()
        
key1.irq(trigger = Pin.IRQ_FALLING, handler = key1_handler)
key2.irq(trigger = Pin.IRQ_FALLING, handler = key2_handler)
key3.irq(trigger = Pin.IRQ_FALLING, handler = key3_handler)
key4.irq(trigger = Pin.IRQ_FALLING, handler = key4_handler)

while True:
    
    if key1_flag == 1:
        print("Button 1")
        key1_flag = 0

    if key2_flag == 1:
        print("Button 2")
        key2_flag = 0
        
    if key3_flag == 1:
        print("Button 3")
        key3_flag = 0
    
    if key4_flag == 1:
        print("Button 4")
        key4_flag = 0
