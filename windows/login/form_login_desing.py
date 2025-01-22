import customtkinter as ctk
from customtkinter import CTkToplevel as ctktl
from windows.gui.design_gui import Gui  # Import gui of application
from PIL import Image
from windows.gui.utility.custom_window import color_pallete
from windows.login.util.encoding_decoding import encrypted, decrypt  # Import encoding/decoding functions
from cache.persistence.repository.auth_user_repository import AuthUserRepositroy  # Import user repository
from cache.persistence.model import Auth_User
from tkinter import messagebox  # Import messagebox

# clase del diseño de la interfaz grafica de usuario
class LoginDesign(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Ventana del login
        self.title('Login')
        self.geometry('800x500')
        self.resizable(0, 0)

        # Imagenes con formato data
        picture_logo_data = Image.open('./pictures/index_3_.png')
        picture_user_data = Image.open('./pictures/person_13924070.png')
        picture_password_data = Image.open('./pictures/cerrar.png')
        picture_google_data = Image.open('./pictures/google-icon.png')

        # Imagenes transformadas a widgets
        picture_logo = ctk.CTkImage(dark_image=picture_logo_data, size=(100, 100), light_image=picture_logo_data)
        picture_user = ctk.CTkImage(dark_image=picture_user_data, light_image=picture_user_data)
        picture_password = ctk.CTkImage(dark_image=picture_password_data, light_image=picture_password_data)
        picture_google = ctk.CTkImage(dark_image=picture_google_data, light_image=picture_google_data)

        # Colores de los widgets
        color, fg_color_window = color_pallete()
        fg_colorsign = '#3498db'
        hover_colorsign = "#E44982"
        text_colorsign = '#000000'
        color_border_sign = '#eceff1'

        # Posicion de los widgets de la izquierda
        padx = 90

        # Icon
        self.iconbitmap('./pictures/index_3_.ico')

        # Frame de la izquierda
        self.image_left = ctk.CTkLabel(
            master=self,
            text='',
            fg_color=color[0],
            width=800,
            height=500,
            #image=picture_logo
        ).place(
            relx=0.5, rely=0.5, anchor='center'
        )

        # Frame de la derecha
        self.frame = ctk.CTkFrame(
            self,
            corner_radius=20,
            width=400,
            height=400,
            bg_color=color[0],
            fg_color="#ffffff"
        )
        self.frame.place(
            relx=0.5, rely=0.5, anchor='center'
        )

        # Etiquetas de encabezado
        self.title_welcome = ctk.CTkLabel(
            master=self.frame,
            text='Inicio de Sesion',
            text_color=text_colorsign,
            anchor='w',
            justify='left',
            font=('Arial Bold', 24)
        ).place(
            x=25, y=50
        )

        self.sign_in_to = ctk.CTkLabel(
            master=self.frame,
            text='Ingresa a tu cuenta',
            text_color='#7E7E7E',
            anchor="w",
            justify="left",
            font=("Arial Bold", 12)
        ).place(
            x=25, y=80
        )

        # Ingreso del email
        self.label_email = ctk.CTkLabel(
            master=self.frame,
            text="  Email:",
            text_color=text_colorsign,
            anchor="w",
            justify="left",
            font=("Arial Bold", 14),
            image=picture_user,
            compound="left"
        ).place(
            x=padx, y=150
        )
        self.entry_email = ctk.CTkEntry(
            master=self.frame,
            width=225,
            fg_color="#EEEEEE",
            border_color=color_border_sign,
            border_width=1,
            text_color="#000000"
        )
        self.entry_email.place(x=padx, y=180)

        # Ingreso del password
        self.label_password = ctk.CTkLabel(
            master=self.frame,
            text="  Password:",
            text_color=text_colorsign,
            anchor="w",
            justify="left",
            font=("Arial Bold", 14),
            image=picture_password,
            compound="left"
        ).place(
            x=padx, y=220
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
        self.entry_password.place(x=padx, y=250)

        # Botones de login
        self.buttom_login = ctk.CTkButton(
            master=self.frame,
            text="Login",
            fg_color=fg_colorsign,
            hover_color=hover_colorsign,
            font=("Arial Bold", 12),
            text_color="#ffffff",
            width=275,
            command=self.handle_login  # Set the command to handle_login
        ).place(
            relx=0.5, rely=0.8, anchor='center'
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
        # ).place(
        #    x=padx, y=350
        # )

        # Boton de nuevo usuario
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
        ).place(
            x=padx - 29, y=350
        )

    def handle_login(self):
        email = self.entry_email.get()
        password = self.entry_password.get()

        # Use the repository to get the user
        repo = AuthUserRepositroy()
        user = repo.getUserByUserName(email)

        if user and decrypt(user.password) == password:
            self.destroy()  # Close the login window
            gui = Gui()  # Import and create an instance of the Gui class
            gui.mainloop()
        else:
            messagebox.showerror("Error de Inicio de Sesión", "Correo electrónico o contraseña inválidos")  # Show error message

    def new_user(self, color_border_sign):
        self.new_user_componete = ctktl()
        self.new_user_componete.geometry("300x400")
        self.resizable(0, 0)
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
        self.label_user.place(x=25, y=10)

        # Entry user
        self.entry_user = ctk.CTkEntry(
            master=self.new_user_componete,
            width=225,
            fg_color="#EEEEEE",
            border_color=color_border_sign,
            border_width=1,
            text_color="#000000"
        )
        self.entry_user.place(x=25, y=40)

        # Label for email entry
        self.label_email = ctk.CTkLabel(
            master=self.new_user_componete,
            text="Email:",
            text_color="#ffffff",
            anchor="w",
            justify="left",
            font=("Arial Bold", 14)
        )
        self.label_email.place(x=25, y=80)

        # Entry email
        self.entry_email = ctk.CTkEntry(
            master=self.new_user_componete,
            width=225,
            fg_color="#EEEEEE",
            border_color=color_border_sign,
            border_width=1,
            text_color="#000000"
        )
        self.entry_email.place(x=25, y=110)

        # Label for password entry
        self.label_password = ctk.CTkLabel(
            master=self.new_user_componete,
            text="Password:",
            text_color="#ffffff",
            anchor="w",
            justify="left",
            font=("Arial Bold", 14)
        )
        self.label_password.place(x=25, y=150)

        # Entry password
        self.entry_password = ctk.CTkEntry(
            master=self.new_user_componete,
            width=225,
            fg_color="#EEEEEE",
            border_color=color_border_sign,
            border_width=1,
            text_color="#000000",
            show="*"
        )
        self.entry_password.place(x=25, y=180)

        # Label for confirm password entry
        self.label_confirm_password = ctk.CTkLabel(
            master=self.new_user_componete,
            text="Confirm Password:",
            text_color="#ffffff",
            anchor="w",
            justify="left",
            font=("Arial Bold", 14)
        )
        self.label_confirm_password.place(x=25, y=220)

        # Confirm password
        self.entry_confirm_password = ctk.CTkEntry(
            master=self.new_user_componete,
            width=225,
            fg_color="#EEEEEE",
            border_color=color_border_sign,
            border_width=1,
            text_color="#000000",
            show="*"
        )
        self.entry_confirm_password.place(x=25, y=250)

        # Create account button
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
        self.button_create_account.place(x=50, y=300)

    def create_account(self):
        user = self.entry_user.get()
        email = self.entry_email.get()
        password = self.entry_password.get()
        confirm_password = self.entry_confirm_password.get()

        if password == confirm_password:
            encrypted_password = encrypted(password)
            new_user = Auth_User(username=user, email=email, password=encrypted_password)
            repo = AuthUserRepositroy()
            try:
                repo.insertUser(new_user)
                self.new_user_componete.destroy()
            except Exception as e:
                if "UNIQUE constraint failed" in str(e):
                    messagebox.showerror("Error de Creación de Cuenta", "El correo electrónico ya existe")
                else:
                    messagebox.showerror("Error de Creación de Cuenta", "Ocurrió un error al crear la cuenta")
        else:
            messagebox.showerror("Error de Creación de Cuenta", "Las contraseñas no coinciden")  # Show error message