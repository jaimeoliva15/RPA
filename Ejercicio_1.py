# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 15:46:09 2024

@author: jog15
"""

import pyautogui
import time


pyautogui.hotkey('win')
time.sleep(2)
pyautogui.typewrite('bloc de notas')
pyautogui.press('enter')
time.sleep(2)
pyautogui.typewrite('¡Hola, mundo!')
pyautogui.press('enter')
time.sleep(2)
pyautogui.typewrite('Ya está acabado')
time.sleep(2)
pyautogui.hotkey('ctrl', 'g')
