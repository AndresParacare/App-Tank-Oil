import customtkinter as ctk
from customtkinter import CTkToplevel as ctktl
from windows.gui.design_gui import Gui # Import gui of application
from PIL import Image
from windows.gui.utility.custom_window import color_pallete
from windows.login.util.encoding_decoding import encrypted, decrypt  # Import encoding/decoding functions
from cache.persistence.repository.auth_user_repository import AuthUserRepositroy  # Import user repository
from cache.persistence.model import Auth_User
#clase del diseño de la interfaz grafica de usuario
class LoginDesign(ctk.CTk):
    def __init__(self):
        super().__init__()

        #Ventana del login
        self.title('Login')
        self.geometry('800x500')
        self.resizable(0,0)

        #Imagenes con formato data
        picture_logo_data = Image.open('./pictures/index_3_.png')
        picture_user_data = Image.open('./pictures/person_13924070.png')
        picture_password_data = Image.open('./pictures/cerrar.png')
        picture_google_data = Image.open('./pictures/google-icon.png')

        #Imagenes transformadas a widgets
        picture_logo = ctk.CTkImage(dark_image=picture_logo_data, size=(100, 100), light_image=picture_logo_data)
        picture_user = ctk.CTkImage(dark_image=picture_user_data, light_image=picture_user_data)
        picture_password = ctk.CTkImage(dark_image=picture_password_data, light_image=picture_password_data)
        picture_google = ctk.CTkImage(dark_image=picture_google_data, light_image=picture_google_data)

        #Colores de los wdigets
        color, fg_color_window = color_pallete()
        fg_colorsign = '#3498db'
        hover_colorsign =  "#E44982"
        text_colorsign = '#000000'
        color_border_sign = '#eceff1'

        #posicion de los widgets de la izquierda
        padx = 90

        # icon
        self.iconbitmap('./pictures/index_3_.ico')

        #Frame de la izquierda
        self.image_left = ctk.CTkLabel(
            master = self,
            text='',
            fg_color=fg_colorsign,
            width=400,
            height=500,
            image = picture_logo
        ).pack(
            expand=True, side="left"
        )

        #Frame de la derecha
        self.frame = ctk.CTkFrame(
            self,
            corner_radius=0,
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
            master=self.frame,
            width=225,
            fg_color="#EEEEEE",
            border_color=color_border_sign,
            border_width=1,
            text_color="#000000"
        )
        self.entry_email.pack(anchor="center", padx=(0, 0))

        #Ingreso del password
        self.label_password = ctk.CTkLabel(
            master=self.frame,
            text="  Password:",
            text_color=text_colorsign,
            anchor="w",
            justify="left",
            font=("Arial Bold", 14), 
            image=picture_password, 
            compound="left"
        ).pack(
            anchor="w", pady=(21, 0), padx=(padx, 0)
        )
        self.entry_password = ctk.CTkEntry(
            master=self.frame, 
            width=225,
            fg_color="#EEEEEE",
            border_color=color_border_sign,
            border_width=1,
            text_color="#000000",
            show="*"
        )
        self.entry_password.pack(anchor="center", padx=(0, 0))
        
        #Botones de login
        self.buttom_login = ctk.CTkButton(
            master= self.frame,
            text="Login",
            fg_color=fg_colorsign,
            hover_color=hover_colorsign,
            font=("Arial Bold", 12),
            text_color="#ffffff",
            width=275,
            command=self.handle_login  # Set the command to handle_login
        ).pack(
            anchor="center", pady=(40, 0), padx=(0, 0)
        )

        # Remove the Google login button
        # self.buttom_google = ctk.CTkButton(
        #    master=self.frame,
        #    text="Login with Google",
        #    fg_color="#EEEEEE",
        #    hover_color="#EEEEEE",
        #    font=("Arial Bold", 9),
        #    text_color="#601E88",
        #    width=275,
        #    image=picture_google
        # ).pack(
        #    anchor="center", pady=(20, 0), padx=(0, 0)
        # )

        #Boton de nuevo usuario
        self.bottom_new_user = ctk.CTkButton(
           master=self.frame,
           text="Crear una nueva cuenta",
           fg_color="#ffffff",
           hover_color="#ffffff",
           font=("Arial Bold", 9),
           text_color="#2a6cee",
           width=100,
           height=10,
           command=lambda: self.new_user(color_border_sign)  # Pass the argument here
        ).pack(
            anchor="w", pady=(5, 0), padx=(padx-29, 0)
            )

    def handle_login(self):
        email = self.entry_email.get()
        password = self.entry_password.get()
        
        # Use the repository to get the user
        repo = AuthUserRepositroy()
        user = repo.getUserByUserName(email)
        
        if user and decrypt(user.password) == password:
            print("Login successful")
            self.destroy()  # Close the login window
            gui = Gui()  # Import and create an instance of the Gui class
            gui.mainloop()
        else:
            print("Login failed")
        
    def new_user(self, color_border_sign):
        self.new_user_componete = ctktl()
        self.new_user_componete.geometry("500x400")
        self.resizable(0,0)
        self.new_user_componete.title("New User")
        self.new_user_componete.configure(bg="#2a6cee")
        
        # Label for user entry
        self.label_user = ctk.CTkLabel(
            master=self.new_user_componete,
            text="Username:",
            text_color="#ffffff",
            anchor="w",
            justify="left",
            font=("Arial Bold", 14)
        )
        self.label_user.pack(anchor="center", pady=(10, 0))

        # entry user
        self.entry_user = ctk.CTkEntry(
            master=self.new_user_componete,
            width=225,
            fg_color="#EEEEEE",
            border_color=color_border_sign,
            border_width=1,
            text_color="#000000"
        )
        self.entry_user.pack(anchor="center", pady=(0, 10))

        # Label for email entry
        self.label_email = ctk.CTkLabel(
            master=self.new_user_componete,
            text="Email:",
            text_color="#ffffff",
            anchor="w",
            justify="left",
            font=("Arial Bold", 14)
        )
        self.label_email.pack(anchor="center", pady=(10, 0))

        # entry email
        self.entry_email = ctk.CTkEntry(
            master=self.new_user_componete,
            width=225,
            fg_color="#EEEEEE",
            border_color=color_border_sign,
            border_width=1,
            text_color="#000000"
        )
        self.entry_email.pack(anchor="center", pady=(0, 10))

        # Label for password entry
        self.label_password = ctk.CTkLabel(
            master=self.new_user_componete,
            text="Password:",
            text_color="#ffffff",
            anchor="w",
            justify="left",
            font=("Arial Bold", 14)
        )
        self.label_password.pack(anchor="center", pady=(10, 0))

        # entry password
        self.entry_password = ctk.CTkEntry(
            master=self.new_user_componete,
            width=225,
            fg_color="#EEEEEE",
            border_color=color_border_sign,
            border_width=1,
            text_color="#000000",
            show="*"
        )
        self.entry_password.pack(anchor="center", pady=(0, 10))

        # Label for confirm password entry
        self.label_confirm_password = ctk.CTkLabel(
            master=self.new_user_componete,
            text="Confirm Password:",
            text_color="#ffffff",
            anchor="w",
            justify="left",
            font=("Arial Bold", 14)
        )
        self.label_confirm_password.pack(anchor="center", pady=(10, 0))

        # confirm password
        self.entry_confirm_password = ctk.CTkEntry(
            master=self.new_user_componete,
            width=225,
            fg_color="#EEEEEE",
            border_color=color_border_sign,
            border_width=1,
            text_color="#000000",
            show="*"
        )
        self.entry_confirm_password.pack(anchor="center", pady=(0, 20))

        # create account button
        self.button_create_account = ctk.CTkButton(
            master=self.new_user_componete,
            text="Crear Cuenta",
            fg_color="#3498db",
            hover_color="#2980b9",
            font=("Arial Bold", 12),
            text_color="#ffffff",
            width=200,
            command=self.create_account
        )
        self.button_create_account.pack(anchor="center", pady=(10, 10))

    def create_account(self):
        user = self.entry_user.get()
        email = self.entry_email.get()
        password = self.entry_password.get()
        confirm_password = self.entry_confirm_password.get()

        if password == confirm_password:
            encrypted_password = encrypted(password)
            new_user = Auth_User(username=user, email=email, password=encrypted_password)
            repo = AuthUserRepositroy()
            repo.insertUser(new_user)
            print(f"Account created for {user} with email {email}")
            self.new_user_componete.destroy()
        else:
            print("Passwords do not match")