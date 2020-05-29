from selenium import webdriver
import time
import pyautogui
from PIL import ImageGrab, ImageOps
import numpy as np

driver = webdriver.Chrome()
driver.get('http://chromedino.com/')

time.sleep(1)
pyautogui.leftClick(1250,30)
time.sleep(3)
pyautogui.typewrite(["SPACE"])


def press_space():
    pyautogui.typewrite(["SPACE"])


def X():
    box = (820, 310, 870, 345 )
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = np.array(grayImage.getcolors())
    print(a.sum())
    return a.sum()


while True:
    if not  X() == 2005:
        press_space()
