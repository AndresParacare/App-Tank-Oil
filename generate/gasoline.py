from typing import Union, Optional

class gasoline():
    def __init__(self, inlet_flow: Optional[Union[int, float]] = 0, output_flow: Optional[Union[int, float]] = 0):
        """ 
        * Q = volumen / tiempo
        * Q = caudal (m³/s o L/s)
        * A es el área de la sección transversal del conducto (m² o cm²)
        * v es la velocidad del fluido (m/s o cm/s)

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
        if(new_speed>0):
            self.inlet_flow = new_speed

    def modify_output_flow(self, new_speed: Optional[Union[int, float]]) -> None:
        """ Modify output flow of the tank """
        if(new_speed>0):
            self.output_flow = new_speed

    def inlet_flow_status(self):
        """ Check if the inlet flow is active """
        return self.inlet_flow != 0
    
    def output_flow_status(self):
        """ Check if the output flow is active """
        return self.output_flow != 0