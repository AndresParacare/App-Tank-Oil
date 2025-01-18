import matplotlib.pyplot as plt # Import pyplot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # Import FigureCanvasTkAgg for we work with canvas
import matplotlib.animation as animation_tools # animation
import customtkinter as ctk # Import customtkinter for custom widgets
import numpy as np

class graph_oil_window():
    #animation):
    def __init__(self, root):
        self._x = np.array([0.5])  # Single bar position
        self._y = np.array([0])  # Initial height of the bar

        fig, self.ax = plt.subplots(figsize=(12, 6.2))  # Change plt.subplot() to plt.subplots()

        self.bar = self.ax.bar(self._x, self._y, color='black')
        self.ax.set(xlim=[0, 1], ylim=[0, 100])

        # Create animation
        #ani = animation_tools.FuncAnimation(fig=fig, func=self.update, frames=40, interval=30)
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
        if frame <= 100:
            height = frame
        else:
            height = 175 - frame  # Decrease from 100 to 75
        self.bar[0].set_height(height)
        return self.bar
    
    def connect_generate():
        # Connect the button to the function that generates the graph
        pass