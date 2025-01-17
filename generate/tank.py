from typing import Union, Optional
from generate.formulas import formulas

class tank():
    def __init__(self, diameter: Optional[Union[float, int]] = 3, lenght: Optional[Union[float, int]]  = 10):
        """The parameters are in meters"""

        # cylinder radius
        self.radius = diameter / 2

        # cylender lenght
        self.lenght = lenght

        # calculate capacity tank
        self.capacity_tank_total = formulas.volume(self.radius, self.lenght)

        # ullage
        self.ullage = formulas.ullage(volume= self.capacity_tank_total)

        # capacity tank
        self.capacity_tank = self.capacity_tank_total - self.ullage

        # tank level
        self.level = 0

    def tank_input(self, input:Optional[Union[float, int]]):
        if(self.capacity_tank_total>self.level):
            #Calculate the new level
            self.level += input
            if(self.level>self.capacity_tank_total):
                self.level = self.capacity_tank_total

    def tank_output(self, output:Optional[Union[float, int]]):
        if(0<self.level):
            #Calculate the output
            self.level -= output
            if(self.level<0):
                self.level = 0

    def tank_state(self):
        return self.level
    
    def set_capacity_tank_tank(self):
        return self.capacity_tank_total
    
    def set_capacity_tank_with_ullage(self):
        return self.capacity_tank
    
    def modify_capacity_tank(self, lenght:Optional[Union[float, int]], radius:Optional[Union[float, int]], volume):
        self.capacity_tank_total = volume(lenght, radius)