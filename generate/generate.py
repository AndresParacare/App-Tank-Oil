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

        # Bloqueo
        self.inlet_padlock = False
        self.outlet_padlock = False

        #thread
        self.thread_input = threading.Thread(target=self.loop_input)
        self.thread_output = threading.Thread(target=self.loop_output)
        self.stop = threading.Event()

    def start_input(self):
        # Start the input thread
        if(self.gasoline.inlet_flow_status()):
            self.inlet_padlock = False
            self.stop.clear()
            self.thread_input.start()
        
    def start_output(self):
        # Start the output thread
        if(self.gasoline.output_flow_status()):
            self.outlet_padlock = False
            self.stop.clear()
            self.thread_output.start()

    def loop_input(self):
        while(True):
            if(self.inlet_padlock):
                time.sleep(1)
                continue
            self.tank.tank_input(self.gasoline.inlet_flow/10)
            time.sleep(1/10)

    def loop_output(self):
        while(True):
            if(self.outlet_padlock):
                time.sleep(1)
                continue
            self.tank.tank_output(self.gasoline.output_flow/10)
            time.sleep(1/10)
            


    def stop_input(self):
        # Stop the input thread
        self.inlet_padlock = True
        #self.gasoline.inlet_flow = 0
        #self.stop.set()
        #self.thread_input.join()

    def stop_output(self):
        # Stop the output thread
        self.outlet_padlock = True
        #self.gasoline.output_flow = 0
        #self.stop.set()
        #self.thread_output.join()

    def get_tank_level(self):
        return self.tank.level

    def get_tank_capacity(self):
        return self.tank.capacity_tank_total

    def get_free_space(self):
        return self.tank.capacity_tank_total - self.tank.level
    
    def modify_capacity_tank(self, capacity: float):
        # Modify the tank capacity
        if capacity > 0:
            self.tank.capacity_tank_total = capacity
            self.tank.ullage = formulas.ullage(volume=capacity)
            self.tank.capacity_tank = self.tank.capacity_tank_total - self.tank.ullage

    def set_inlet_flow(self, flow: float):
        self.gasoline.inlet_flow = flow

    def set_output_flow(self, flow: float):
        self.gasoline.output_flow = flow

    def get_ullage(self):
        return self.tank.get_ullage()
    
    #-----------------#
    #  graph of tank  #
    #-----------------#
    def graph_oil_window(self, root):

        self._x = np.array([0.5])  # Single bar position
        self._y = np.array([0])  # Initial height of the bar

        sns.set(style="whitegrid")  # Apply seaborn style to the plot
        colors = sns.color_palette("husl", 1)  # Use seaborn color palette

        self.fig, self.ax = plt.subplots(figsize=(12, 6.2))  # Change plt.subplot() to plt.subplots()

        self.bar = self.ax.bar(self._x, self._y, color='black', alpha=0.85)  # Use the color black and make the bar transparent
        self.ax.set(xlim=[0, 1], ylim=[0, self.tank.capacity_tank_total])
        self.ax.set_title('Tank Level', fontsize=20)
        self.ax.set_ylabel('Level (L)', fontsize=14, labelpad=30)
        self.ax.grid(True, linestyle='--', alpha=0.7)  # Show grid
        self.ax.set_facecolor('#f0f0f0')  # Set the background color of the plot

        # Modify sticks
        self.ax.set_xticks([])
        self.ax.set_yticks(np.linspace(0, self.tank.capacity_tank_total,11))  # Set y ticks to b
        self.ax.set_facecolor('#f0f0f0')

        # Design graph 
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['bottom'].set_visible(False)
        self.ax.tick_params(axis='x', colors='black')
        self.ax.tick_params(axis='y', colors='black')

        # Identify ullage
        self.ax.axhline(y=self.tank.capacity_tank, color='red', linestyle='--', linewidth=2, alpha=0.7)
        self.ax.text(1.03,self.tank.capacity_tank, f'Ullage\n{self.tank.get_ullage():.2f}', fontsize=12, color='red', ha='center')

        # Create animation
        ani = animation_tools.FuncAnimation(self.fig, self.update, frames=np.arange(0, 175), interval=30, blit=True)

        # Create a Tkinter canvas
        canvas = FigureCanvasTkAgg(self.fig, master=root) # Create the Tkinter canvas with the figure
        canvas.draw() # Draw the canvas, the figure will be painted here
        canvas.get_tk_widget().pack(
            side=ctk.TOP,
            fill=ctk.BOTH,
            expand=True
        ) # Put the canvas in the Tkinter window

    def update(self, frame):
        """Update the bar chart"""
        if self.tank.level <= (self.tank.capacity_tank_total - self.tank.ullage):
            self.bar[0].set_color((0, 0, 0, 0.5))  # Change the bar color to black and make it transparent
        else:
            self.bar[0].set_color((1, 0, 0, 0.5))  # Change the bar color to red and make it transparent
        height = self.tank.level  # Use the tank level for the bar height
        self.bar[0].set_height(height)
        return self.bar
    
    def reset_graph(self):
        self.fig.clf()
        self.ax = self.fig.subplots()
        self.bar = self.ax.bar(self._x, self._y, color='black', alpha=0.85)
        self.ax.set(xlim=[0, 1], ylim=[0, self.tank.capacity_tank_total])
        self.ax.set_title('Tank Level', fontsize=20)
        self.ax.set_ylabel('Level (L)', fontsize=14, labelpad=30)
        self.ax.grid(True, linestyle='--', alpha=0.7)
        self.ax.set_facecolor('#f0f0f0')
        self.ax.set_xticks([])
        self.ax.set_yticks(np.linspace(0, self.tank.capacity_tank_total,11))
        self.ax.set_facecolor('#f0f0f0')
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['bottom'].set_visible(False)
        self.ax.tick_params(axis='x', colors='black')

