import RPi.GPIO as GPIO
import time
import random

def setup_led_at_pin(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.setup(pin, GPIO.HIGH)
    pwm = GPIO.PWM(pin, 2000)
    pwm.start(0)
    return pwm

def setBrightness(pwm, val):  # 0 ~ 100 values since 0 ~ 100 only for duty cycle
    pwm.ChangeDutyCycle(val)

def close(all_pwm):
    for pwm in all_pwm:
        pwm.close()
    GPIO.cleanup()

def on(pwm):
    GPIO.output(40, 1)

GPIO.setmode(GPIO.BOARD)
pwmR = setup_led_at_pin(40)
on(pwmR)
time.sleep(4)
close(pwmR)