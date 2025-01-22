from customtkinter import CTkImage, CTkFont # Import CTkImage and CTkFont from customtkinter
from customtkinter import CTk as ctk #Class for customtkinter widgets
from customtkinter import CTkFrame as ctkf #Class for customtkinter widgets
from customtkinter import CTkButton as ctkb # Import CTkButton for the button widget
from customtkinter import CTkLabel as ctkl # Import CTkLabel for the label widget
from customtkinter import CTkEntry as ctken # Import CTkEntry for the entry widget
from customtkinter import CTkProgressBar as ctksb # Import CTkProgressBar for the progress bar widget
from customtkinter import CTkToplevel as ctkid # Import CTkInputDialog for the input dialog widget
from windows.gui.utility.custom_window import color_pallete #Function for color pallete
from generate.generate import generate # funcionality of the buttoms
from PIL import Image # library for image processing
from typing import Union, Optional
import time
import threading # Import threading

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
        picture_logo_data = Image.open('.\pictures\index_3_.png')
        #Images to widgets
        self.picture_logo = CTkImage(
            picture_logo_data,
            size=(50, 50)
            )
        self.picture_play = CTkImage(
            dark_image=picture_play_data,
            light_image=picture_play_data
        )
        self.picture_stop = CTkImage(
            dark_image=picture_stop_data,
            light_image=picture_stop_data
        )

        #Create the main window of the application
        self.title("App Tank Oil")
        color, fg_color_window = color_pallete()

        # icon 
        self.iconbitmap('.\pictures\index_3_.ico')


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
        
        #loop of level
        self.loop_level_show = threading.Thread(target=self.loop_level)
        self.loop_level_show.start()
        

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
        self.logo = ctkl(
            self.frame_up,
            text="",
            width=50,
            height=50,
            corner_radius=0,
            fg_color=color[0],
            image=self.picture_logo
        )
        self.logo.place(
            relx=0.45, rely=0.5, anchor='center'  # Adjusted relx to 0.85
        )

        self.logo_titule = ctkl(
            self.frame_up,
            text="App Tank Oil",
            width=150,
            height=50,
            corner_radius=0,
            fg_color=color[0],
            text_color=color[7],
            font=("Arial", 20, "bold")
            )
        self.logo_titule.place(
            relx=0.53, rely=0.5, anchor='center'
            )

    def label_dasboard(self, color):
        """Create a label for identify dashboard"""
        self.l_dashboard = ctkl(
            self,
            width=90,
            height=30,
            text="DASHBOARD",
            fg_color="#222323",
            font=CTkFont(size=26, weight="bold")  # Set font size to 20 and make it bold
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

        #graph_oil_window(self.frame_center)
        self.generator.graph_oil_window(self.frame_center)
    
    def create_frame_right(self, color):
        """Create the right frame of the application."""
        self.frame_right = ctkf(
            self,
            width=340,
            height=420,
            corner_radius=20,
            fg_color=color[1]
        )
        self.frame_right.place(
            relx=0.84, rely=0.578, anchor='center'
        )

        self.label_control = ctkl(
            self.frame_right,
            width=100,
            height=20,
            text="Control Panel",
            fg_color=color[1],
            font=CTkFont(size=22, weight="bold")  # Set font size to 20 and make it bold
        )

        self.label_control.place(
            relx=0.5, rely=0.15, anchor='center'
        )

        self.b_info = ctkb(
            self.frame_right,
            text="Info",
            width=50,
            height=35,
            corner_radius=30,
            fg_color=color[0],
            command= self.dialog_info
        )

        self.b_info.place(
            relx=0.5, rely=0.9, anchor='center'
        )

        self.l_inlet_flow = ctkl(
            self.frame_right,
            width=100,
            height=20,
            text="Inlet Flow: ",
            fg_color=color[1],
            font=CTkFont(size=16)  # Set font size to 20
        )

        self.l_inlet_flow.place(
            relx=0.2, rely=0.3, anchor='center'
        )
        self.entry_inlet_flow = ctken(
            self.frame_right,
            width=100,
            height=20,
            fg_color=color[5],
            text_color=color[7],
            font=CTkFont(size=16)  # Set font size to 20
            )
        
        self.entry_inlet_flow.place(
            relx=0.55, rely=0.3, anchor='center'
            )
        
        self.b_apply_inlet = ctkb(
            self.frame_right,
            text="Apply",
            width=30,
            height=20,
            corner_radius=30,
            fg_color=color[0],
            command= self.connect_entryTOinlet_flow
        )

        self.b_apply_inlet.place(
            relx=0.82, rely=0.3, anchor='center'
        )
        
        self.l_output_flow = ctkl(
            self.frame_right,
            width=100,
            height=20,
            text="Output Flow: ",
            fg_color=color[1],
            font=CTkFont(size=16)  # Set font size to 20
        )

        self.l_output_flow.place(
            relx=0.2, rely=0.42, anchor='center'
        )
        self.entry_output_flow = ctken(
            self.frame_right,
            width=100,
            height=20,
            fg_color=color[5],
            text_color=color[7],
            font=CTkFont(size=16)  # Set font size to 20
            )
        
        self.entry_output_flow.place(
            relx=0.55, rely=0.42, anchor='center'
            )
        
        self.b_apply_output = ctkb(
            self.frame_right,
            text="Apply",
            width=30,
            height=20,
            corner_radius=30,
            fg_color=color[0],
            command=self.connect_entryTOoutput_flow
        )

        self.b_apply_output.place(
            relx=0.82, rely=0.42, anchor='center'
        )

        self.l_capacity = ctkl(
            self.frame_right,
            width=100,
            height=20,
            text="Tank Capacity: ",
            fg_color=color[1],
            font=CTkFont(size=16)  # Set font size to 20
        )

        self.l_capacity.place(
            relx=0.2, rely=0.56, anchor='center'
        )

        self.entry_capacity = ctken(
            self.frame_right,
            width=100,
            height=20,
            fg_color=color[5],
            text_color=color[7],
            font=CTkFont(size=16)  # Set font size to 20
            )
        
        self.entry_capacity.place(
            relx=0.55, rely=0.56, anchor='center'
            )
        
        self.b_apply_capacity = ctkb(
            self.frame_right,
            text="Apply",
            width=30,
            height=20,
            corner_radius=30,
            fg_color=color[0],
            command=self.connect_entryTOcapacity
        )

        self.b_apply_capacity.place(
            relx=0.82, rely=0.56, anchor='center'
        )
        
        self.l_capacity_tank = ctkl(
            self.frame_right,
            width=100,
            height=20,
            text=f"Total Tank Capacity: {self.get_tank_capacity():.2f} L",
            fg_color=color[1],
            font=CTkFont(size=16)  # Set font size to 20
        )

        self.l_capacity_tank.place(
            relx=0.5, rely=0.64, anchor='center'
        )

        self.pro_bar_tank = ctksb(
            self.frame_right,
            width=250,
            height=20,
            corner_radius=10,
            fg_color=color[5],
            progress_color=color[7]
        )

        self.pro_bar_tank.place(
            relx=0.5, rely=0.71, anchor='center'
        )

        self.l_level_tank = ctkl(
            self.frame_right,
            width=100,
            height=20,
            text=f"Level: {self.get_tank_level():.2f} l",
            fg_color=color[1],
            font=CTkFont(size=12)  # Set font size to 20
        )

        self.l_level_tank.place(
            relx=0.2, rely=0.77, anchor='center'
        )

        self.l_free_space = ctkl(
            self.frame_right,
            width=100,
            height=20,
            text=f"free space: {self.get_free_space():.2f} l",
            fg_color=color[1],
            font=CTkFont(size=12)  # Set font size to 20
        )

        self.l_free_space.place(
            relx=0.76, rely=0.77, anchor='center'
        )

        self.l_inlet_flow_value = ctkl(
            self.frame_right,
            width=100,
            height=20,
            text=f"Inlet Flow: {self.generator.gasoline.inlet_flow:.2f} L/s",
            fg_color=color[1],
            font=CTkFont(size=16)  # Set font size to 20
        )

        self.l_inlet_flow_value.place(
            relx=0.5, rely=0.35, anchor='center'
        )

        self.l_output_flow_value = ctkl(
            self.frame_right,
            width=100,
            height=20,
            text=f"Output Flow: {self.generator.gasoline.output_flow:.2f} L/s",
            fg_color=color[1],
            font=CTkFont(size=16)  # Set font size to 20
        )

        self.l_output_flow_value.place(
            relx=0.5, rely=0.48, anchor='center'
        )
    
    def command_buttom_start_init(self):
        self.generator.start_input()

    def command_buttom_stop_init(self):
        self.generator.stop_input()
    
    def command_buttom_start_output(self):
        self.generator.start_output()

    def command_buttom_stop_output(self):
        self.generator.stop_output()

    def get_tank_level(self) -> float:
        return self.generator.get_tank_level()

    def get_tank_capacity(self) -> float:
        return self.generator.get_tank_capacity()

    def get_free_space(self) -> float:
        return self.generator.get_free_space()
    
    def modify_capacity(self, capacity: Optional[Union[float, int]]):
        self.generator.modify_capacity_tank(capacity=capacity)

    def connect_entryTOcapacity(self):
        new_capacity = float(self.entry_capacity.get())
        self.modify_capacity(new_capacity)
        self.l_capacity_tank.configure(text=f"Total Tank Capacity: {self.get_tank_capacity():.2f} L")
        self.l_free_space.configure(text=f"Free space: {self.get_free_space():.2f} l")
        self.l_level_tank.configure(text=f"Level: {self.get_tank_level():.2f} l")
        self.reset_graph()

    def connect_entryTOinlet_flow(self):
        new_inlet_flow = float(self.entry_inlet_flow.get())
        self.generator.gasoline.inlet_flow = new_inlet_flow
        self.l_inlet_flow_value.configure(text=f"Inlet Flow: {new_inlet_flow:.2f} L/s")
        print(f"New inlet flow: {new_inlet_flow}")

    def connect_entryTOoutput_flow(self):
        new_output_flow = float(self.entry_output_flow.get())
        self.generator.gasoline.output_flow = new_output_flow
        self.l_output_flow_value.configure(text=f"Output Flow: {new_output_flow:.2f} L/s")
        print(f"New output flow: {new_output_flow}")

    def loop_level(self):
        while(True):
            time.sleep(1)
            self.l_level_tank.configure(text=f"Level: {self.get_tank_level():.2f} l")
            self.l_free_space.configure(text=f"Free space: {self.get_free_space():.2f} l")

    def reset_graph(self):
        self.frame_center.destroy()
        color, fg_color_window = color_pallete()
        self.create_frame_center(color=color)

    def dialog_info(self):
        tank_capacity = self.get_tank_capacity()
        tank_level = self.get_tank_level()
        free_space = self.get_free_space()
        ullage = self.generator.get_ullage()
        inlet_flow = self.generator.gasoline.inlet_flow
        output_flow = self.generator.gasoline.output_flow

        info_message = (
            f"Tank Capacity: {tank_capacity:.2f} L\n"
            f"Tank Level: {tank_level:.2f} L\n"
            f"Free Space: {free_space:.2f} L\n"
            f"Ullage: {ullage:.2f} L\n"
            f"Inlet Flow: {inlet_flow:.2f} L/s\n"
            f"Output Flow: {output_flow:.2f} L/s"
        )

        self.info = ctkid(
            #fg_color=self._fg_color,
            #title="System Info",
            #text=info_message,
            #fg_color=self._fg_color
        )
        
        self.info.geometry("300x300")
        self.info.title("System Info")
        self.info.iconbitmap('.\pictures\index_3_.ico')

        self.info_label = ctkl(
            self.info,
            width=100,
            height=20,
            text=info_message,
            font=CTkFont(size=12),  # Set font size to 20
        )

        self.info_label.place(
            relx=0.5, rely=0.5, anchor='center'
        )
