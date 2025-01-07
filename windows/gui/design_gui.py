from customtkinter import CTk as ctk #Class for customtkinter widgets
from customtkinter import CTkFrame as ctkf #Class for customtkinter widgets
from customtkinter import CTkButton as ctkb # Import CTkButton for the button widget
from customtkinter import CTkLabel as ctkl # Import CTkLabel for the label widget
from windows.gui.utility.custom_window import color_pallete #Function for color pallete
from windows.gui.widget.graphTankModule import graph_oil_window #Function for graph tank module

class Gui(ctk):
    def __init__(self):
        super().__init__()
        """
        Create the main window of the application 
        and the frames of the application.
        """ 
        #Create the main window of the application
        self.title("Titulo")
        color, fg_color_window = color_pallete()

        #size window
        self.pl_x = -5
        self.pl_y = 0
        self.window_width = self.winfo_screenwidth()-10
        self.window_height = self.winfo_screenheight()-80
        self.window_size = str(self.window_width) + "x" + str(self.window_height)\
        + "+" + str(self.pl_x) + "+" + str(self.pl_y)
        self.geometry(self.window_size)

        #Color of the window
        self._set_appearance_mode("dark")
        self._fg_color = fg_color_window
        
        #Create the frames of the application
        self.create_frame_up(color)
        self.bar_gray(color)
        self.create_frame_center(color)
        self.create_frame_right(color)
        

    def create_frame_up(self, color):
        """Create the upper frame of the application.
        this also creates a button and a label.
        """
        self.frame_up = ctkf(
            self,
            width=1270,
            height=70,
            corner_radius=0,
            fg_color=color[0]
        )
        self.frame_up.pack(
            expand=True,
            anchor='n'
        )
        
        # Create a button ten frames to the left of the right edge of frame_up
        self.button_up_right = ctkb(
            self.frame_up,
            text="",
            width=50,
            height=50,
            corner_radius=90,
            fg_color=color[1]
        )
        self.button_up_right.place(
            relx=0.95, rely=0.5, anchor='center'  # Adjusted relx to 0.85
        )

        # Create a buttom to the notifcation
        self.button_notification = ctkb(
            self.frame_up,
            text="",
            width=40,
            height=40,
            corner_radius=90,
            fg_color=color[1]
        )
        self.button_notification.place(
            relx=0.9, rely=0.5, anchor='center'
        )

        # Create a label to the left of the frame_up
        self.label_up = ctkl(
            self.frame_up,
            text="Name of the application",
            fg_color=color[1]
        )
        self.label_up.place(
            relx=0.1, rely=0.5, anchor='center'
        )

    def bar_gray(self, color):
        """Create bar with gray color"""
        self.bar_gray = ctkf(
            self,
            width=1270,
            height=2,
            corner_radius=0,
            fg_color=color[0]
        )
        self.bar_gray.place(
            relx= 0.5,
            rely= 0.2,
            anchor='center'
        )

    def create_frame_center(self, color):
        """Create the center frame of the application."""
        self.frame_center = ctkf(
            self,
            width=800,
            height=420,
            corner_radius=20,
            fg_color=color[1]
        )
        self.frame_center.place(
            relx=0.35, 
            rely=0.578, 
            anchor='center'
        )

        graph_oil_window(self.frame_center)
    
    def create_frame_right(self, color):
        """Create the right frame of the application."""
        self.frame_right = ctkf(
            self,
            width=320,
            height=420,
            corner_radius=20,
            fg_color=color[1]
        )
        self.frame_right.place(
            relx=0.84, rely=0.578, anchor='center'
        )