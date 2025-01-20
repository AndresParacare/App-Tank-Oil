from generate.gasoline import gasoline # Manage gasoline
from generate.formulas import formulas # have to import this to use the formulas
from generate.tank import tank # Manage tank capacity and fuel level
import time # Manage time and date
import threading # for multithreading

#++++++++++++++++++++++#
# library for the tank #
#++++++++++++++++++++++#
import matplotlib.pyplot as plt # Import pyplot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # Import FigureCanvasTkAgg for we work with canvas
import matplotlib.animation as animation_tools # animation
import customtkinter as ctk # Import customtkinter for custom widgets
import numpy as np
import seaborn as sns  # Import seaborn

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
            self.tank.tank_input(self.gasoline.inlet_flow/10)
            time.sleep(1/10)
            print(self.tank.level)
            if(self.gasoline.inlet_flow == 0):
                break;

    def loop_output(self):
        while(True):
            self.tank.tank_output(self.gasoline.output_flow/10)
            time.sleep(1/10)
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

    def get_tank_level(self):
        return self.tank.level

    def get_tank_capacity(self):
        return self.tank.capacity_tank_total

    def get_free_space(self):
        return self.tank.capacity_tank_total - self.tank.level
    
    def modify_capacity_tank(self, capacity: float):
        # Modify the tank capacity
        if (capacity > 0):
            self.tank.capacity_tank_total = capacity
            self.tank.ullage = formulas.ullage(volume= self.capacity_tank_total)
            self.tank.capacity_tank = self.tank.capacity_tank_total - self.tank.ullage
    
    #-----------------#
    #  graph of tank  #
    #-----------------#
    def graph_oil_window(self, root):

        self._x = np.array([0.5])  # Single bar position
        self._y = np.array([0])  # Initial height of the bar

        sns.set(style="whitegrid")  # Apply seaborn style to the plot
        colors = sns.color_palette("husl", 1)  # Use seaborn color palette

        fig, self.ax = plt.subplots(figsize=(12, 6.2))  # Change plt.subplot() to plt.subplots()

        self.bar = self.ax.bar(self._x, self._y, color='black', alpha=0.85)  # Use the color black and make the bar transparent
        self.ax.set(xlim=[0, 1], ylim=[0, self.tank.capacity_tank_total])

        # Create animation
        ani = animation_tools.FuncAnimation(fig, self.update, frames=np.arange(0, 175), interval=30, blit=True)

        # Create a Tkinter canvas
        canvas = FigureCanvasTkAgg(fig, master=root) # Create the Tkinter canvas with the figure
        canvas.draw() # Draw the canvas, the figure will be painted here
        canvas.get_tk_widget().pack(
            side=ctk.TOP,
            fill=ctk.BOTH,
            expand=True
        ) # Put the canvas in the Tkinter window

    def update(self, frame):
        """Update the bar chart"""
        height = self.tank.level  # Use the tank level for the bar height
        self.bar[0].set_height(height)
        self.bar[0].set_color('red')  # Change the bar color to red and make it transparent
        return self.bar