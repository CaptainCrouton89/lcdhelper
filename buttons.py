import RPi.GPIO as GPIO
from time import sleep
import random

BUTTON_L_PIN = 13
BUTTON_C_PIN = 15
BUTTON_R_PIN = 11

def button_callback_L(channel):
    print("L Button was pushed!")

def button_callback_C(channel):
    print("C Button was pushed!")

def button_callback_R(channel):
    print("R Button was pushed!")

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

GPIO.setup(BUTTON_L_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(BUTTON_C_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(BUTTON_R_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

GPIO.add_event_detect(BUTTON_L_PIN,GPIO.RISING,callback=button_callback_L) # Setup event on pin 10 rising edge
GPIO.add_event_detect(BUTTON_C_PIN,GPIO.RISING,callback=button_callback_C) # Setup event on pin 10 rising edge
GPIO.add_event_detect(BUTTON_R_PIN,GPIO.RISING,callback=button_callback_R) # Setup event on pin 10 rising edge

message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up
