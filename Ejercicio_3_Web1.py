# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 15:18:30 2024

@author: jog15
"""

import requests
from bs4 import BeautifulSoup
# URL de la página web de noticias deportivas "Marca"
url = 'https://www.marca.com/'
# Realizamos una solicitud GET para obtener el contenido de la página
response = requests.get(url)
# Verificamos si la solicitud fue exitosa
if response.status_code == 200:
# Parseamos el contenido HTML de la página
    soup = BeautifulSoup(response.text, 'html.parser')
    # Buscamos las noticias relacionadas con "Topuria"
    noticias = soup.find_all('a', string=lambda text: text and 'Alonso'
in text)
# Imprimimos los titulares y enlaces de las noticias encontradas
    if noticias:
        print("Noticias relacionadas con Alonso:")
        for noticia in noticias:
            print("- Título:", noticia.text)
            print(" Enlace:", noticia['href'])
    else:
        print("No se encontraron noticias relacionadas con Alonso.")
else:
    print("Error al obtener el contenido de la página:",
response.status_code)