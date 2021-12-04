import RPi.GPIO as GPIO
from time import sleep
import random

GPIO.setmode(GPIO.BOARD)             # choose BCM or BOARD  
GPIO.setup(40, GPIO.OUT)           # set GPIO24 as an output   
  
try:  
    while True:  
        GPIO.output(40, 1)         # set GPIO24 to 1/GPIO.HIGH/True  
        sleep(0.5)                 # wait half a second  
        GPIO.output(40, 0)         # set GPIO24 to 0/GPIO.LOW/False  
        sleep(0.5)                 # wait half a second  
  
except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
    GPIO.cleanup()                 # resets all GPIO ports used by this program  