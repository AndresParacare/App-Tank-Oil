from customtkinter import CTkImage # Import CTkImage from customtkinter
from customtkinter import CTk as ctk #Class for customtkinter widgets
from customtkinter import CTkFrame as ctkf #Class for customtkinter widgets
from customtkinter import CTkButton as ctkb # Import CTkButton for the button widget
from customtkinter import CTkLabel as ctkl # Import CTkLabel for the label widget
from windows.gui.utility.custom_window import color_pallete #Function for color pallete
from windows.gui.widget.graphTankModule import graph_oil_window #Function for graph tank module
from generate.generate import generate # funcionality of the buttoms
from PIL import Image # library for image processing

class Gui(ctk):
    def __init__(self):
        super().__init__()
        """
        Create the main window of the application 
        and the frames of the application.
        """ 
        # Activate class generate
        self.generator = generate()
        self.generator.gasoline.inlet_flow = 2
        self.generator.gasoline.output_flow = 1.5

        #Images with format
        picture_play_data = Image.open(".\pictures\play.png")
        picture_stop_data = Image.open(".\pictures\stop.png")

        #Images to widgets
        self.picture_play = CTkImage(
            dark_image=picture_play_data,
            light_image=picture_play_data
        )
        self.picture_stop = CTkImage(
            dark_image=picture_stop_data,
            light_image=picture_stop_data
        )

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
        self.buttom_stop_init(color)
        self.buttom_start_init(color)
        self.buttom_stop_out(color)
        self.buttom_start_out(color)
        self.label_dasboard(color)
        

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

    def label_dasboard(self, color):
        """Create a label for identify dashboard"""
        self.l_dashboard = ctkl(
            self,
            width=90,
            height=30,
            text="Dashboard",
            fg_color=color[1]
        )

        self.l_dashboard.place(
            relx=0.1, rely=0.154, anchor='center'
        )

    def buttom_stop_init(self, color):
        """Buttom to the dashboard"""
        self.b_stop_init = ctkb(
            self,
            text="",
            width=35,
            height=35,
            corner_radius=90,
            fg_color=color[1],
            image=self.picture_stop,
            command=self.command_buttom_stop_init
        )

        self.b_stop_init.place(
            relx=0.95, rely=0.154, anchor='center'
        )

    def buttom_start_init(self, color):
        """Buttom to the pictures"""
        self.b_start_init = ctkb(
            self,
            text="",
            width=35,
            height=35,
            corner_radius=90,
            fg_color=color[1],
            image=self.picture_play,
            command=self.command_buttom_start_init
        )

        self.b_start_init.place(
            relx=0.9, rely=0.154, anchor='center'
        )
    
    def buttom_stop_out(self, color):
        """Buttom to the dashboard"""
        self.b_stop_out = ctkb(
            self,
            text="",
            width=35,
            height=35,
            corner_radius=90,
            fg_color=color[1],
            image=self.picture_stop,
            command=self.command_buttom_stop_output
        )

        self.b_stop_out.place(
            relx=0.8, rely=0.154, anchor='center'
        )

    def buttom_start_out(self, color):
        """Buttom to the pictures"""
        self.b_start_out = ctkb(
            self,
            text="",
            width=35,
            height=35,
            corner_radius=90,
            fg_color=color[1],
            image=self.picture_play,
            command= self.command_buttom_start_output
        )

        self.b_start_out.place(
            relx=0.75, rely=0.154, anchor='center'
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
    
    def command_buttom_start_init(self):
        self.generator.start_input()

    def command_buttom_stop_init(self):
        self.generator.stop_input()
    
    def command_buttom_start_output(self):
        self.generator.start_output()

    def command_buttom_stop_output(self):
        self.generator.stop_output()