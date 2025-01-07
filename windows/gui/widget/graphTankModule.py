import matplotlib.pyplot as plt # Import pyplot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # Import FigureCanvasTkAgg for we work with canvas
import matplotlib.animation as animation_tools # animation
from windows.gui.utility.animation import animation #Function for color pallete
import customtkinter as ctk # Import customtkinter for custom widgets

class graph_oil_window(animation):
    def __init__(self, root):
        fig, self.ax = plt.subplots(figsize=(12, 6.2))  # Change plt.subplot() to plt.subplots()
        super().__init__()

        #Create animation
        ani = animation_tools.FuncAnimation(fig=fig, func=self.update, frames=40, interval=30)
        
        # Create a Tkinter canvas
        canvas = FigureCanvasTkAgg(fig, master=root) # Create the Tkinter canvas with the figure
        canvas.draw() # Draw the canvas, the figure will be painted here
        canvas.get_tk_widget().pack(
            side=ctk.TOP,
            fill=ctk.BOTH,
            expand=True
        ) # Put the canvas in the Tkinter window