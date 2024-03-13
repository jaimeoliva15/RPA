# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 16:43:15 2024

@author: jog15
"""

import pyautogui
import time
import cv2

pyautogui.hotkey('win')
time.sleep(2)
pyautogui.write('word')
pyautogui.press('enter')
time.sleep(2)
# Capturar una captura de pantalla
captura = pyautogui.screenshot()
# Guardar la captura de pantalla como un archivo de imagen temporal
captura_path = "captura_temporal.png"
captura.save(captura_path)
x, y = pyautogui.locateCenterOnScreen('nuevo_doc.png',confidence=0.9)
pyautogui.moveTo(x, y, 2, pyautogui.easeOutQuad)
pyautogui.click(x, y,clicks=2,interval=0.2)
time.sleep(2)
pyautogui.write('¡Hola, tonto si lo lees!')
# Capturar una captura de pantalla
captura = pyautogui.screenshot()
# Guardar la captura de pantalla como un archivo de imagen temporal
captura_path = "captura_temporal.png"
captura.save(captura_path)
x, y = pyautogui.locateCenterOnScreen('guardar_icon.png',confidence=0.9)
pyautogui.moveTo(x, y, 2, pyautogui.easeOutQuad)
pyautogui.click(x, y,clicks=1,interval=0.2)
time.sleep(2)
# Capturar una captura de pantalla
captura = pyautogui.screenshot()
# Guardar la captura de pantalla como un archivo de imagen temporal
captura_path = "captura_temporal.png"
captura.save(captura_path)
x, y = pyautogui.locateCenterOnScreen('elegir_carpeta.png',confidence=0.9)
pyautogui.moveTo(x, y, 2, pyautogui.easeOutQuad)
pyautogui.click(x, y,clicks=1,interval=0.2)
time.sleep(2)
# Capturar una captura de pantalla
captura = pyautogui.screenshot()
# Guardar la captura de pantalla como un archivo de imagen temporal
captura_path = "captura_temporal.png"
captura.save(captura_path)
x, y = pyautogui.locateCenterOnScreen('escritorio.png',confidence=0.9)
pyautogui.moveTo(x, y, 2, pyautogui.easeOutQuad)
pyautogui.click(x, y,clicks=1,interval=0.2)
time.sleep(2)
# Capturar una captura de pantalla
captura = pyautogui.screenshot()
# Guardar la captura de pantalla como un archivo de imagen temporal
captura_path = "captura_temporal.png"
captura.save(captura_path)
x, y = pyautogui.locateCenterOnScreen('guardar.png',confidence=0.9)
pyautogui.moveTo(x, y, 2, pyautogui.easeOutQuad)
pyautogui.click(x, y,clicks=1,interval=0.2)
time.sleep(2)
# Capturar una captura de pantalla
captura = pyautogui.screenshot()
# Guardar la captura de pantalla como un archivo de imagen temporal
captura_path = "captura_temporal.png"
captura.save(captura_path)
x, y = pyautogui.locateCenterOnScreen('cerrar_word.png',confidence=0.9)
pyautogui.moveTo(x, y, 2, pyautogui.easeOutQuad)
pyautogui.click(x, y,clicks=1,interval=0.2)
time.sleep(2)