import RPi.GPIO as GPIO
import time
import random

def setup_led_at_pin(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.setup(pin, GPIO.HIGH)
    pwm = GPIO.PWM(pin, 2000)
    pwm.start(0)
    return pwm

def setColor(pwm, val):  # 0 ~ 100 values since 0 ~ 100 only for duty cycle
    pwm.ChangeDutyCycle(val)

def close(all_pwm):
    for pwm in all_pwm:
        pwm.close()
    GPIO.cleanup()


GPIO.setmode(GPIO.BOARD)
pwmR = setup_led_at_pin(40)
setColor(pwmR, 100)
time.sleep(4)
close(pwmR)