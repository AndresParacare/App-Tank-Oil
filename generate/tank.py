import numpy as np
from typing import Union, Optional

class tank():
    def __init__(self, diameter: Optional[Union[float, int]] = 3, lenght: Optional[Union[float, int]]  = 10):
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

        # tank level
        self.level = 0

    def tank_input(self, input:Optional[Union[float, int]]):
        if(self.capacity_tank>self.level):
            self.level += input

    def tank_output(self, output:Optional[Union[float, int]]):
        if(0<self.level):
            self.level -= output

    def tank_status(self):
        return self.level
    
    def set_capacity_tank(self):
        return self.capacity_tank
    
    def modify_capacity_tank(self, lenght:Optional[Union[float, int]], radius:Optional[Union[float, int]], volume):
        self.capacity_tank = volume(lenght, radius)