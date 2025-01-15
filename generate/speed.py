from typing import Union, Optional

class speed():
    def __init__(self, inlet_flow: Optional[Union[int, float]] = 0, output_flow: Optional[Union[int, float]] = 0):
        """ 
        Q = volumen / tiempo
        Q = caudal (m³/s o L/s)
        A es el área de la sección transversal del conducto (m² o cm²)
        v es la velocidad del fluido (m/s o cm/s)
        variables a crear:
        -----------------
        caudal_ent: caudal entrada
        Scaudal_sal: caudal salida"""
        #inlet flow
        self. inlet_flow = inlet_flow

        #output flow
        self.output_flow = output_flow

    def modify_inlet_flow(self, new_speed: Optional[Union[int, float]]) -> None:
        """ Modify inlet flow of the tank """
        self.inlet_flow = new_speed

    def modify_output_flow(self, new_speed: Optional[Union[int, float]]) -> None:
        """ Modify output flow of the tank """
        self.output_flow = new_speed


