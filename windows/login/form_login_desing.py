import customtkinter as ctk
from PIL import Image

#clase del diseño de la interfaz grafica de usuario
class LoginDesign(ctk.CTk):
    def __init__(self):
        super().__init__()

        #Ventana del login
        self.title('Login')
        self.geometry('800x500')
        self.resizable(0,0)

        #Imagenes con formato data
        picture_user_data = Image.open(
            '.\pictures\person_13924070.png'
        )

        picture_password_data = Image.open(
            '.\pictures\cerrar.png'
        )

        picture_google_data = Image.open(
            '.\pictures\google-icon.png'
        )
        #picture_login_part_right_data = Image.open()

        #Imagenes transformadas a widgets
        picture_user = ctk.CTkImage(
            dark_image=picture_user_data,
            light_image=picture_user_data
        )
        picture_password = ctk.CTkImage(
            dark_image=picture_password_data,
            light_image=picture_password_data
        )

        picture_google = ctk.CTkImage(
            dark_image=picture_google_data,
            light_image=picture_google_data
        )

        #Colores de los wdigets
        fg_colorsign = '#3498db'
        hover_colorsign =  "#E44982"
        text_colorsign = '#000000'
        color_border_sign = '#eceff1'

        #posicion de los widgets de la izquierda
        padx = 90

        #Frame de la izquierda
        self.image_left = ctk.CTkLabel(
            master = self,
            text='',
            fg_color=fg_colorsign,
            width=400,
            height=500
            #image = picture_login_part_right
        ).pack(
            expand=True, side="left"
        )

        #Frame de la derecha
        self.frame = ctk.CTkFrame(
            self,
            width=400,
            height=500,
            fg_color="#ffffff"
        )
        self.frame.propagate(0)
        self.frame.pack(
            expand = True,
            side = 'right'
            )
        
        #Etiquetas de encabezado
        self.title_welcome = ctk.CTkLabel(
            master= self.frame,
            text = 'Inicio de Sesion',
            text_color= text_colorsign,
            anchor = 'w',
            justify='left',
            font=('Arial Bond', 24)
        ).pack(
            anchor="w", pady=(50, 5), padx=(25, 0)
        )

        self.sign_in_to = ctk.CTkLabel(
            master = self.frame,
            text='Ingresa a tu cuenta',
            text_color='#7E7E7E', 
            anchor="w", 
            justify="left", 
            font=("Arial Bold", 12)
        ).pack(
            anchor="w", padx=(25, 0)
        )

        #Ingreso del email
        self.label_email = ctk.CTkLabel(
            master=self.frame, 
            text="  Email:", 
            text_color=text_colorsign, 
            anchor="w", 
            justify="left", 
            font=("Arial Bold", 14), 
            image=picture_user, 
            compound="left"
        ).pack(
            anchor="w", pady=(38, 0), padx=(padx, 0)
        )
        self.entry_email = ctk.CTkEntry(
            master = self.frame,
            width=225,
            fg_color="#EEEEEE",
            border_color= color_border_sign,
            border_width=1,
            text_color="#000000"
        ).pack(
            anchor="center", padx=(0, 0)
        )

        #Ingreso del password
        self.label_password = ctk.CTkLabel(
            master=self.frame,
            text="  Password:",
            text_color=text_colorsign,
            anchor="w",
            justify="left",
            font=("Arial Bold", 14), 
            image = picture_password, 
            compound="left"
            ).pack(
                anchor="w", pady=(21, 0), padx=(padx, 0)
            )
        
        self.entry_password = ctk.CTkEntry(
            master=self.frame, 
            width=225,
            fg_color="#EEEEEE",
            border_color= color_border_sign,
            border_width=1,
            text_color="#000000",
            show="*"
            ).pack(
                anchor="center", padx=(0, 0)
            )
        
        #Botones de login
        self.buttom_login = ctk.CTkButton(
            master= self.frame,
            text="Login",
            fg_color=fg_colorsign,
            hover_color=hover_colorsign,
            font=("Arial Bold", 12),
            text_color="#ffffff",
            width=275
        ).pack(
            anchor="center", pady=(40, 0), padx=(0, 0)
        )

        #Boton de google
        self.buttom_google = ctk.CTkButton(
           master=self.frame,
           text="Login with Google",
           fg_color="#EEEEEE",
           hover_color="#EEEEEE",
           font=("Arial Bold", 9),
           text_color="#601E88",
           width=275,
           image=picture_google
        ).pack(
            anchor="center", pady=(20, 0), padx=(0, 0)
            )
        
        #Boton de nuevo usuario
        self.bottom_new_user = ctk.CTkButton(
           master=self.frame,
           text="Crear una nueva cuenta",
           fg_color="#ffffff",
           hover_color="#ffffff",
           font=("Arial Bold", 9),
           text_color="#2a6cee",
           width=100,
           height=10

        ).pack(
            anchor="w", pady=(5, 0), padx=(padx-29, 0)
            )