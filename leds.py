import RPi.GPIO as GPIO
from time import sleep
import random

LED_R_PIN = 40
LED_Y_PIN = 38
LED_G_PIN = 36
LED_B_PIN = 32

GPIO.setmode(GPIO.BOARD)  
GPIO.setup(LED_R_PIN, GPIO.OUT)
GPIO.setup(LED_Y_PIN, GPIO.OUT)
GPIO.setup(LED_G_PIN, GPIO.OUT)
GPIO.setup(LED_B_PIN, GPIO.OUT)
  
try:  
    while True:  
        GPIO.output(LED_R_PIN, 1)         # set GPIO24 to 1/GPIO.HIGH/True  
        sleep(0.5)                 # wait half a second  
        GPIO.output(LED_R_PIN, 0)         # set GPIO24 to 0/GPIO.LOW/False  
        sleep(0.5)                 # wait half a second  
        GPIO.output(LED_Y_PIN, 1)         # set GPIO24 to 1/GPIO.HIGH/True  
        sleep(0.5)                 # wait half a second  
        GPIO.output(LED_Y_PIN, 0)         # set GPIO24 to 0/GPIO.LOW/False  
        sleep(0.5)
        GPIO.output(LED_G_PIN, 1)         # set GPIO24 to 1/GPIO.HIGH/True  
        sleep(0.5)                 # wait half a second  
        GPIO.output(LED_G_PIN, 0)         # set GPIO24 to 0/GPIO.LOW/False  
        sleep(0.5)
        GPIO.output(LED_B_PIN, 1)         # set GPIO24 to 1/GPIO.HIGH/True  
        sleep(0.5)                 # wait half a second  
        GPIO.output(LED_B_PIN, 0)         # set GPIO24 to 0/GPIO.LOW/False  
        sleep(0.5)
  
except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
    GPIO.cleanup()                 # resets all GPIO ports used by this program  