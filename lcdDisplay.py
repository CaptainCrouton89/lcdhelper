from RPLCD import CharLCD # type: ignore
from RPi import GPIO # type: ignore
import time
import threading


class LCD():
    """LCD Helper class for controlling the Adafruit 16x2 LCD screen"""

    def __init__(self, lcd, cols=16) -> None:
        self.lcd = lcd
        self.scrolling = None
        self._num_cols = cols
        self._text: str = ""
        self._scroll_speed: float = 0.3
        self._start_pause: float = 0.5
        self.clear()
        self.home()

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

    def display(self):
        self.lcd.clear()
        self.home()
        self.lcd.write_string(self._text)

    def write_to_lcd(self, framebuffer):
        """Write the framebuffer out to the specified LCD."""
        lcd.home()
        for row in framebuffer:
            self.lcd.write_string(row.ljust(self._num_cols)[:self._num_cols])
            self.lcd.write_string('\r\n')

    def loop_string(self, strings, framebuffer, row, delay=0.2):
        padding = ' ' * self._num_cols
        s = strings + padding
        for i in range(len(s) - self._num_cols + 1):
            framebuffer[row] = s[i:i+self._num_cols]
            self.write_to_lcd(framebuffer)
            time.sleep(delay)

        
    def _init_scroll(self) -> None:
        """Plays message on repeat
        speed: amount of time spent before next character is shown
        start_pause: how long to leave at start message before scrolling
        """
        self.scrolling = threading.Thread(target=self._scroll_text, daemon=True)
        self.scrolling.exit = False
        self.start_scroll()

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
        self.lcd.write_string(self._text)
        while self.scrolling.is_scrolling:
            time.sleep(self._start_pause)
            for i in range(len(self._text) - 16):
                self.lcd.scrollDisplayLeft()
                time.sleep(self._speed)
                if self.scrolling.exit == True:
                    break

if __name__ == '__main__':
    char_lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=16, rows=2, pin_rs=26, pin_e=24, pins_data=[22, 18, 16, 12])
    # char_lcd.write_string(u'Hello world!')

    lcd = LCD(char_lcd)
    lcd.clear()
    framebuffer = [
        "Hello world",
        ""
    ]
    long_string = "This statement is simply way too long to display"
    while True:
        lcd.loop_string(long_string, framebuffer, 1, .3)
    # lcd.display()
    # lcd._init_scroll()
    # lcd.start_scroll()

    lcd.clear()

