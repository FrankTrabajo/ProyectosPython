from tkinter import ttk
from tkinter import *
from tkinter import Tk, Label, LabelFrame, Entry, PhotoImage, Canvas
import sqlite3
import usuario
import ventanaInicio
import ventanaResgistro
import ventaInicioSesion

class Menu:

    def __init__(self, root):
        self.menu = root
        self.menu.title("Hostal Cruz Sol")
        self.menu.resizable(1, 1)  # Activa la redimension de la ventana. Para desactivarla (0,0)
        self.menu.wm_iconbitmap('recursos/cruzSol.ico')

        titulo = Label(self.menu, text="HOSTAL CRUZ SOL", font=('Calibri', 16, 'bold'), fg='#000080')
        titulo.pack()

        # Creación de un contenedor Canvas para la imagen
        canvas_frame = LabelFrame(self.menu, text="", font=('Calibri', 16, 'bold'), padx=20, pady=20, borderwidth=0)
        canvas_frame.pack()

        # Carga de la imagen
        self.filename = PhotoImage(file='recursos/cruzSol.png')
        canvas = Canvas(canvas_frame, width=400, height=100)
        canvas.create_image(110, 0, anchor='nw', image=self.filename)
        canvas.pack()

        frame = LabelFrame(self.menu, text="MENÚ", font=('Calibri', 16, 'bold'), padx=70, pady=20)
        frame.configure(labelanchor="n")
        frame.pack()

        self.btn_sesion = Button(frame, text="Iniciar sesion", borderwidth=0, bg='#ABB9D8',foreground="#000000", activeforeground="#FFA500", command=lambda: (self.iniciarSesion()))
        self.btn_sesion.place(x=40,y=50)
        self.btn_sesion.grid(row=0, column=2, pady=10, padx=50)

    def iniciarSesion(self):
        self.sesion = ventaInicioSesion.VentanaPrincipal(self)

    def enviar_a_segundo_plano(self):
        self.menu.withdraw()  # Oculta la ventana principal


if __name__ == '__main__':
    root = Tk()  # Instancia de la ventana principal
    app = Menu(root)  # Se envia a la clase VentanaPrincipal el control sobre la ventana root
    root.geometry("400x400+240+120")
    root.mainloop()  # Comenzamos el bucle de aplicacion, es como un while True
