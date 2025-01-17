from generate.gasoline import gasoline
from generate.formulas import formulas
from generate.tank import tank

class generate():
    def __init__(self):
        # Initialize the class

        # Create the class gassoline
        self.gasoline = gasoline()

        # Create the class tank
        self.tank = tank()

    def start_input(self):
        while(self.gasoline.inlet_flow_status()):
            self.tank.tank_input(self.gasoline.inlet_flow)

    def stop_input(self):
        pass


    def start_output(self):
        while(self.gasoline.output_flow_status()):
            self.tank.tank_output(self.gasoline.output_flow)

    def stop_output(self):
        pass