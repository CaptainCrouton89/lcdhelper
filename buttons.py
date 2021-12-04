import RPi.GPIO as GPIO # type: ignore

BUTTON_L_PIN = 13
BUTTON_C_PIN = 15
BUTTON_R_PIN = 11

def button_callback_L(channel):
    print("L Button was pushed!")

def button_callback_C(channel):
    print("C Button was pushed!")

def button_callback_R(channel):
    print("R Button was pushed!")

def add_func_to_button(func, button_pin):
    GPIO.add_event_detect(button_pin, GPIO.RISING, callback=func)

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

GPIO.setup(BUTTON_L_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUTTON_C_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUTTON_R_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

if __name__ == '__main__':
    add_func_to_button(BUTTON_C_PIN, button_callback_C)
    add_func_to_button(BUTTON_L_PIN, button_callback_L)
    add_func_to_button(BUTTON_R_PIN, button_callback_R)

    message = input("Press enter to quit\n\n") # Run until someone presses enter
    GPIO.cleanup() # Clean up
