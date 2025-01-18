from generate.gasoline import gasoline # Manage gasoline
from generate.formulas import formulas # have to import this to use the formulas
from generate.tank import tank # Manage tank capacity and fuel level
import time # Manage time and date
import psutil # for system monitoring
import threading # for multithreading

class generate():
    def __init__(self):
        # Initialize the class

        # Create the class gassoline
        self.gasoline = gasoline()

        # Create the class tank
        self.tank = tank()

        #thread
        self.thread_input = threading.Thread(target=self.loop_input)
        self.thread_output = threading.Thread(target=self.loop_output)
        self.stop = threading.Event()

    def start_input(self):
        # Start the input thread
        if(self.gasoline.inlet_flow_status()):
            self.stop.clear()
            self.thread_input.start()
        
    def start_output(self):
        # Start the output thread
        if(self.gasoline.output_flow_status()):
            self.stop.clear()
            self.thread_output.start()

    def loop_input(self):
        while(True):
            self.tank.tank_input(self.gasoline.inlet_flow)
            time.sleep(1)
            print(self.tank.level)
            if(self.gasoline.inlet_flow == 0):
                break;

    def loop_output(self):
        while(True):
            self.tank.tank_output(self.gasoline.output_flow)
            time.sleep(1)
            print(self.tank.level)
            if(self.gasoline.output_flow == 0):
                break;


    def stop_input(self):
        self.gasoline.inlet_flow = 0
        self.stop.set()
        self.thread_input.join()

    def stop_output(self):
        self.gasoline.output_flow = 0
        self.stop.set()
        self.thread_output.join()
