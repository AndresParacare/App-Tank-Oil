# delete this module (in the future)
import customtkinter as ctk

class DraggableButton(ctk.CTkButton):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.bind("<Button-1>", self.on_click)
        self.bind("<B1-Motion>", self.on_drag)

    def on_click(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def on_drag(self, event):
        x = self.winfo_x() + event.x - self.start_x
        y = self.winfo_y() + event.y - self.start_y
        self.place(x=x, y=y)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Ventana con Botón Movible")
        self.geometry("400x300")

        # Crear el botón arrastrable
        self.draggable_button = DraggableButton(self, text="Arrástrame")
        self.draggable_button.place(x=100, y=100)

app = App()
app.mainloop()
