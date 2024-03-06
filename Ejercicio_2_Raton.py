# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 16:49:43 2024

@author: jog15
"""

import pyautogui
import time
time.sleep(5)
a = pyautogui.position() # Cambia las coordenadas según s
print(a)
pyautogui.moveTo(898, 1048, duration=0.5)
pyautogui.rightClick()
pyautogui.moveTo(918, 821, duration=0.5)
pyautogui.click()
pyautogui.moveTo(983, 555, duration=0.5)
time.sleep(2)
pyautogui.click()
pyautogui.write('bitcoin')
pyautogui.press('enter')
time.sleep(2)
im1 = pyautogui.screenshot('my_screenshot.png')