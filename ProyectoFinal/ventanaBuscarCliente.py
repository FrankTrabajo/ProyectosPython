import sqlite3
from tkinter import *



class buscaCliente:

    def __init__(self, ventana_inicio):
        self.ventana_inicio = ventana_inicio
        self.ventana_busca = Toplevel()
        self.ventana_busca.title("Hostal Cruz Sol")
        self.ventana_busca.resizable(1, 1)
        self.ventana_busca.wm_iconbitmap('recursos/cruzSol.ico')
        self.ventana_busca.geometry("1300x600+240+120")
