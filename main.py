import tkinter as tk    #Para la interfaz gráfica
from tkinter import ttk #Para agregar más estilos
import socket           #Para la comunicación en red
import threading 
import time             #Para manejar tiempos de espera

# ---CONFIGURACIÓN---
IP_ESP32 = "192.168.20.51"   #Cambia por la IP que de el ESP32
PUERTO = 80

# ---CLASE DE DATOS (Para practicar)---
class DatosSensor:
    def __init__(self, valor):
        self.valor = valor