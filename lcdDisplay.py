#! /usr/bin/python
from Adafruit_CharLCD import Adafruit_CharLCD
from RPLCD import CharLCD
from RPi import GPIO
import time
import threading


class LCD():
    """LCD Helper class for controlling the Adafruit 16x2 LCD screen"""

    def __init__(self, lcd) -> None:
        self.lcd = lcd
        self.scrolling = None
        self._text: str = ""
        self._scroll_speed: float = 0.3
        self._start_pause: float = 0.5

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text

    @property
    def scroll_speed(self):
        return self._scroll_speed

    @scroll_speed.setter
    def scroll_speed(self, scroll_speed: float):
        if scroll_speed > 1:
            scroll_speed = 1
        if scroll_speed <= 0:
            scroll_speed = .05
        self._scroll_speed = scroll_speed

    @property
    def start_pause(self):
        return self._start_pause

    @start_pause.setter
    def start_pause(self, start_pause: float):
        if start_pause not in range(0, 3):
            start_pause = 0
        self._start_pause = start_pause

    def home(self):
        self.lcd.home()

    def clear(self):
        self.lcd.clear()

    def display(self, state):
        if state:
            self.lcd.displaydisplay()
        else:
            self.lcd.noDisplay()

    def _init_scroll(self, **kwargs) -> None:
        """Plays message on repeat
        speed: amount of time spent before next character is shown
        start_pause: how long to leave at start message before scrolling
        """
        self.scroll_speed = kwargs["scroll_speed"]
        self.start_pause = kwargs["start_pause"]
        self.scrolling = threading.Thread(target=self._scroll_text, daemon=True)
        self.scrolling.exit = False
        self.scrolling.start_scroll()

    def start_scroll(self):
        self.scrolling.is_scrolling = True

    def stop_scroll(self):
        self.scrolling.is_scrolling = False

    def quit_scroll(self):
        """Use `stop_scroll` instead unless you wish to restart the scrolling thread."""
        self.scrolling.exit = True

    def _scroll_text(self):
        self.clear()
        self.home()
        self.lcd.message = self.text
        while self.scrolling.is_scrolling:
            time.sleep(self._start_pause)
            for i in range(len(self._text) - 16):
                self.lcd.scrollDisplayLeft()
                time.sleep(self._speed)
                if self.scrolling.exit == True:
                    break

if __name__ == '__main__':
    lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=16, rows=2, pin_rs=7, pin_e=8, pins_data=[18, 23, 24, 25])
    lcd.write_string(u'Hello world!')

    # lcd = LCD(Adafruit_CharLCD())
    # lcd.text = "Hello world"
    # lcd._init_scroll()

