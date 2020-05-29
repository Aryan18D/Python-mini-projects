# download chromedriver before running this code.
from selenium import webdriver
import time
import pyautogui
from PIL import ImageGrab, ImageOps
import numpy as np

driver = webdriver.Chrome()
driver.get('http://chromedino.com/') # you can type any URL here because the code works offline page of chrome
# Make sure your pc is offline as the coordinates are set for offline Chrome dino

time.sleep(1)
pyautogui.leftClick(1250,30)
time.sleep(3)
pyautogui.typewrite(["SPACE"])


def press_space():
    pyautogui.typewrite(["SPACE"])


def X():
    box = (825, 310, 875, 345 )
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = np.array(grayImage.getcolors())
    print(a.sum())
    return a.sum()
    print(a.sum())

while True:
    k = X()
    if not  k == 2005:
        press_space()
    if k == 1750: # night mode starts
        break
while True:  # night mode
    k = X()
    if not k == 1750:
        press_space()
    if k == 2005:  # light mode starts
        break
while True:   # light mode
    k = X()
    if not  k == 2005:
        press_space()
    if k == 1750:
        break
