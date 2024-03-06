# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 16:30:08 2024

@author: jog15
"""

import pyautogui
import time
time.sleep(3)
# Mueve el mouse a una posición específica en el escritorio
a = pyautogui.position() # Cambia las coordenadas según s
print(a)
pyautogui.moveTo(812, 15, duration=0.5)
pyautogui.click()
pyautogui.moveTo(308, 745, duration=0.5)
pyautogui.dragTo(527, 294, duration=0.5)
pyautogui.moveTo(173, 723, duration=0.5)
pyautogui.dragTo(412, 300, duration=0.5)
pyautogui.moveTo(527, 294, duration=0.5)
pyautogui.dragTo(308, 745, duration=0.5)
pyautogui.moveTo(412, 300, duration=0.5)
pyautogui.dragTo(173, 723, duration=0.5)
pyautogui.mouseUp()