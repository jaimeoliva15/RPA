# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 16:32:37 2024

@author: jog15
"""

import pyautogui
import cv2
import time
time.sleep(5)
# Capturar una captura de pantalla
captura = pyautogui.screenshot()
# Guardar la captura de pantalla como un archivo de imagen temporal
captura_path = "captura_temporal.png"
captura.save(captura_path)
# Cargar la imagen a buscar usando OpenCV
imagen_a_buscar = cv2.imread("Test_icon.png")
# Buscar la imagen en la captura de pantalla
resultado = cv2.matchTemplate(cv2.cvtColor(cv2.imread(captura_path),
cv2.COLOR_BGR2GRAY),
cv2.cvtColor(imagen_a_buscar,
cv2.COLOR_BGR2GRAY),
cv2.TM_CCOEFF_NORMED)
# Obtener las coordenadas de la imagen si se encuentra
_, _, _, max_loc = cv2.minMaxLoc(resultado)
x, y = max_loc

# Hacer clic en el centro de la imagen si se encuentra
if resultado.max() > 0.9:
    centro_x = x + imagen_a_buscar.shape[1] // 2
    centro_y = y + imagen_a_buscar.shape[0] // 2
    pyautogui.moveTo(centro_x, centro_y, 2, pyautogui.easeOutQuad)
    pyautogui.click(centro_x, centro_y,clicks=2,interval=0.2)
    time.sleep(2)
    pyautogui.alert("Imagen encontrada y clic realizando en el centro.")
else:
    time.sleep(2)
    pyautogui.alert("Imagen no encontrada.")
# Eliminar el archivo de imagen temporal
import os
os.remove(captura_path)