# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 15:46:09 2024

@author: jog15
"""

import pyautogui
import time
import pyperclip


pyautogui.hotkey('win')
time.sleep(2)
pyautogui.write('bloc de notas')
pyautogui.press('enter')
time.sleep(2)
pyautogui.write('¡Hola, mundo!')
pyautogui.press('enter')
time.sleep(2)
pyperclip.copy('VIVA ESPAÑA')
pyautogui.hotkey('ctrl', 'v')
# pyperclip.paste()
time.sleep(2)
pyautogui.hotkey('ctrl', 'g')

