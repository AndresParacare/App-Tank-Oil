import numpy as np

class tank():
    def __init__(self, diameter: float = 3, lenght: float = 10):
        """The parameters are in meters"""
        # Tanques Cilíndricos Horizontales
        # Longitud: Entre 2 y 10 metros (aproximadamente 78 a 394 pulgadas)
        # Diámetro: Entre 1 y 3 metros (aproximadamente 39 a 118 pulgadas)

        # Basado en la API (American Petroleum Institute): La norma API 650 es 
        # una de las más utilizadas a nivel mundial para el diseño y construcción 
        # de tanques de almacenamiento de petróleo y derivados. Establece requisitos 
        # para materiales, diseño, fabricación, pruebas e inspección.

        # cylinder radius
        self.radius = diameter / 2

        # cylender lenght
        self.lenght = lenght

        # formula of volume
        volume = lambda r, l: np.pi * (r**2) * l

        # calculate capacity tank
        self.capacity_tank = volume(self.radius, self.lenght)