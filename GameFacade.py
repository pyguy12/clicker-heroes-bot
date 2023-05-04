import time
import pyautogui
import numpy as np
from PIL import ImageGrab

class GameFacade:
    def __init__(self, game_window_title=None):
        self.game_window = None
        if game_window_title is not None:
            self.locate_game_window(game_window_title)

    def locate_game_window(self, title):
        try:
            self.game_window = pyautogui.getWindowsWithTitle(title)[0]
            self.game_window.activate()
        except IndexError:
            print(f"Window with title '{title}' not found.")
            self.game_window = None

    def capture_screen(self, region=None):
        if self.game_window is not None:
            region = (
                self.game_window.left,
                self.game_window.top,
                self.game_window.width,
                self.game_window.height,
            )
        screenshot = ImageGrab.grab(bbox=region)
        return np.array(screenshot)

    def click(self, x, y):
        pyautogui.click(x, y)

    def press_key(self, key):
        pyautogui.press(key)

    def hold_key(self, key, duration=None):
        pyautogui.keyDown(key)
        if duration:
            time.sleep(duration)
            pyautogui.keyUp(key)

    def release_key(self, key):
        pyautogui.keyUp(key)
