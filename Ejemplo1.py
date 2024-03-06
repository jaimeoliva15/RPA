# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pyautogui
import time
# Esperar unos segundos antes de comenzar para que tengas tiempo de cambiar
#a la ventana de la aplicación de procesamiento de texto
time.sleep(5)
# Escribir un mensaje utilizando la función typewrite()
pyautogui.typewrite('¡Hola, mundo!\n')
# Presionar la tecla Enter para cambiar de línea
pyautogui.press('enter')
# Escribir otro mensaje
pyautogui.typewrite('Este es un ejemplo de PyAutoGUI.')
# Cerrar la aplicación de procesamiento de texto
# Nota: Este comando es específico para la aplicación y puede necesitar ser
# ajustado según la aplicación que estés utilizando
pyautogui.hotkey('ctrl', 'g')