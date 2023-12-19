import tkinter as tk
from tkinter import ttk
import os
from tkinter import messagebox

class Menu:
    def __init__(self, root):
        self.root = root
        self.root.title("Buscaminas")
        self.root.geometry('540x600')
        self.root.configure(background="DimGray")
         # Ruta a la imagen
        image_path = "data/imagen.png"
        image = tk.PhotoImage(file=image_path)

        # Ajusta el tamaño de la imagen según tus necesidades
        image = image.subsample(2)  # Cambia el factor según sea necesario

        # Inserta la imagen en una etiqueta
        label = ttk.Label(self.root, image=image)
        label.image = image  # Asegúrate de mantener una referencia a la imagen
        #label.pack(padx=10, pady=10)
        label.place(x=0,y=0)
        label_texto=ttk.Label(self.root,text="Bienvenido",bg=None,font=("Arial",60))
        label_texto.pack(anchor="center",pady=10)
        
        self.juego_principiante = tk.Button(self.root, text= "Modo Principiante", command=lambda:self.iniciar_partida(8,8,10))
        self.juego_principiante.pack(padx=30, pady=90)
        self.juego_principiante.place(x=30,y=390,width=200,height=30)
        self.juego_principiante.configure(foreground="white",background="green")

        self.juego_intermedio = tk.Button(self.root, text= "Modo Intermedio", command=lambda:self.iniciar_partida(16,16,40))
        self.juego_intermedio.pack(padx=30, pady=90)
        self.juego_intermedio.place(x=30,y=425, width=200,height=30)
        self.juego_intermedio.configure(foreground="black",background="yellow")

        self.juego_experto = tk.Button(self.root, text= "Modo experto", command=lambda:self.iniciar_partida(16,30,99))
        self.juego_experto.pack(padx=30, pady=90)
        self.juego_experto.place(x=30,y=460,width=200,height=30)
        self.juego_experto.configure(foreground="white",background="red")

        self.juego_personalizado = tk.Button(self.root, text="Modo personalizado", command=self.configurar_partida)
        self.juego_personalizado.pack(padx=30, pady=90)
        self.juego_personalizado.place(x=30,y=495,width=200,height=30)
        self.juego_personalizado.configure(foreground="white",background="blue")
   
    def configurar_partida(self):
        config_window = tk.Toplevel(self.root)
        config_window.title("Configurar Partida")

        config_window.label_filas = tk.Label(config_window, text="Filas:")
        config_window.label_filas.grid(row=0, column=0, padx=10, pady=10)
        config_window.entry_filas = tk.Entry(config_window)
        config_window.entry_filas.grid(row=0, column=1, padx=10, pady=10)

        config_window.label_columnas = tk.Label(config_window, text="Columnas:")
        config_window.label_columnas.grid(row=1, column=0, padx=10, pady=10)
        config_window.entry_columnas = tk.Entry(config_window)
        config_window.entry_columnas.grid(row=1, column=1, padx=10, pady=10)

        config_window.label_minas = tk.Label(config_window, text="Minas:")
        config_window.label_minas.grid(row=2, column=0, padx=10, pady=10)
        config_window.entry_minas = tk.Entry(config_window)
        config_window.entry_minas.grid(row=2, column=1, padx=10, pady=10)

        config_window.btn_confirmar = tk.Button(config_window, text="Confirmar", command=lambda: self.confirmar(config_window))
        config_window.btn_confirmar.grid(row=3, column=0, columnspan=2, pady=10)

    def confirmar(self, config_window):
        try:
            filas = int(config_window.entry_filas.get())
            columnas = int(config_window.entry_columnas.get())
            minas = int(config_window.entry_minas.get())

            if filas <= 0 or columnas <= 0 or minas <= 0:
                messagebox.showerror("Error", "Ingrese valores válidos para Filas, Columnas y Minas.")
            elif minas >= filas * columnas:
                messagebox.showerror("Error", "La cantidad de minas debe ser menor que el tamaño del tablero.")
            else:
                self.iniciar_partida(filas, columnas, minas)
                #config_window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos para Filas, Columnas y Minas.")

    def iniciar_partida(self, filas, columnas, minas):
        self.root.destroy()
        llamada= "python3 game/maintest.py " + str(filas) + " " + str(columnas) + " " + str(minas)
        os.system(llamada)

if __name__ == "__main__":
    root = tk.Tk()
    app = Menu(root)
    root.mainloop()
