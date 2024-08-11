import cv2
import numpy as np
import pyautogui
import mss
from time import sleep 

def capture_screen():
    with mss.mss() as sct:
        screenshot = sct.grab(sct.monitors[0])
        screenshot_np = np.array(screenshot)
        gray_screenshot = cv2.cvtColor(screenshot_np, cv2.COLOR_BGRA2GRAY)
    return gray_screenshot

def load_template(template_path):
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    width, height = template.shape[::-1]
    return template, width, height

def find_template(gray_screenshot, template):
    res = cv2.matchTemplate(gray_screenshot, template, cv2.TM_CCOEFF_NORMED)
    _, _, _, max_loc = cv2.minMaxLoc(res)
    return max_loc

def click(top_left, width, height):
    center_x = top_left[0] + width // 2
    center_y = top_left[1] + height // 2
    pyautogui.click(center_x, center_y)

# Open the browser
template, width, height = load_template('templates/chrome.png')
gray_screenshot = capture_screen()
top_left = find_template(gray_screenshot, template)
click(top_left, width, height)

# Open a new tab
sleep(1)
pyautogui.hotkey('ctrl', 't')
# Go to the YouTube Music tab
pyautogui.write('https://music.youtube.com/')
pyautogui.press('enter')

sleep(5)
# Search for music
template, width, height = load_template('templates/search_bar.png')
gray_screenshot = capture_screen()
top_left = find_template(gray_screenshot, template)
click(top_left, width, height)
pyautogui.write('Shape of You')
pyautogui.press('enter')

# Click on the music
sleep(5)
template, width, height = load_template('templates/music.png')
gray_screenshot = capture_screen()
top_left = find_template(gray_screenshot, template)
click(top_left, width, height)
