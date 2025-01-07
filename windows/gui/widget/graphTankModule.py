import matplotlib.pyplot as plt # Import pyplot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # Import FigureCanvasTkAgg for we work with canvas
import matplotlib.animation as animation # animation
import customtkinter as ctk # Import customtkinter for custom widgets


class graph_oil_window():
    def __init__(self,root):
        fig, ax = plt.subplots(figsize = (12, 6.2))  # Change plt.subplot() to plt.subplots()
        ax.plot([1,2,3,4,5], [1,4,9,16,25])  # plotting the data
        
        # Create a Tkinter canvas
        canvas = FigureCanvasTkAgg(fig, master = root) # Create the Tkinter canvas with the figure
        canvas.draw() # Draw the canvas, the figure will be painted here
        canvas.get_tk_widget().pack(
            side = ctk.TOP,
            fill = ctk.BOTH,
            expand = True
        ) # Put the canvas in the Tkinter window