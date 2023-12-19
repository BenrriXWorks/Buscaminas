import tkinter as tk
import os
from tkinter import messagebox

class Menu:
    def __init__(self, root):
        # Define el frame
        self.root = root
        self.root.title("Buscaminas")
        self.root.geometry('800x800')
        root.resizable(False, False)
        
        # Ruta a la imagen
        image_path = "data/ExplosionBackground.png"
        image = tk.PhotoImage(file=image_path)
        # Coloca la imagen de fondo como un label
        background_label = tk.Label(root, image=image)
        background_label.place(relwidth=1, relheight=1)  # Establece el tamaño del Label para llenar la ventana
        background_label.image = image
        
        # Boton de modo principiante
        self.juego_principiante = tk.Button(self.root, text= "Modo Principiante", font=("Fixedsys", 18), command=lambda:self.iniciar_partida(8,8,10))
        self.juego_principiante.pack(padx=30, pady=90)
        self.juego_principiante.place(x=30,y=390,width=300,height=30)
        self.juego_principiante.configure(foreground="Black",background="#2ecc71")

        # Boton de modo intermedio
        self.juego_intermedio = tk.Button(self.root, text= "Modo Intermedio", font=("Fixedsys", 18), command=lambda:self.iniciar_partida(16,16,40))
        self.juego_intermedio.pack(padx=30, pady=90)
        self.juego_intermedio.place(x=30,y=425, width=300,height=30)
        self.juego_intermedio.configure(foreground="black",background="#3498db")

        # Boton de modo experto
        self.juego_experto = tk.Button(self.root, text= "Modo experto", font=("Fixedsys", 18), command=lambda:self.iniciar_partida(16,30,99))
        self.juego_experto.pack(padx=30, pady=90)
        self.juego_experto.place(x=30,y=460,width=300,height=30)
        self.juego_experto.configure(foreground="black",background="#e74c3c")

        # Boton de modo personalizado
        self.juego_personalizado = tk.Button(self.root, text="Modo personalizado", font=("Fixedsys", 18), command=self.configurar_partida)
        self.juego_personalizado.pack(padx=30, pady=90)
        self.juego_personalizado.place(x=30,y=495,width=300,height=30)
        self.juego_personalizado.configure(foreground="black",background="#9b59b6")
   
    def configurar_partida(self) -> None:
        '''Coloca el menu de configurar la partida y guarda la entrada'''
        config_window = tk.Toplevel(self.root)
        config_window.title("Configurar Partida")

        # Campo de filas
        config_window.label_filas = tk.Label(config_window, text="Filas:")
        config_window.label_filas.grid(row=0, column=0, padx=10, pady=10)
        config_window.entry_filas = tk.Entry(config_window)
        config_window.entry_filas.grid(row=0, column=1, padx=10, pady=10)

        # Campo de columnas
        config_window.label_columnas = tk.Label(config_window, text="Columnas:")
        config_window.label_columnas.grid(row=1, column=0, padx=10, pady=10)
        config_window.entry_columnas = tk.Entry(config_window)
        config_window.entry_columnas.grid(row=1, column=1, padx=10, pady=10)

        # Campo de minas
        config_window.label_minas = tk.Label(config_window, text="Minas:")
        config_window.label_minas.grid(row=2, column=0, padx=10, pady=10)
        config_window.entry_minas = tk.Entry(config_window)
        config_window.entry_minas.grid(row=2, column=1, padx=10, pady=10)

        # Boton de confirmar
        config_window.btn_confirmar = tk.Button(config_window, text="Confirmar", command=lambda: self.confirmar(config_window))
        config_window.btn_confirmar.grid(row=3, column=0, columnspan=2, pady=10)

    def confirmar(self, config_window) -> None:
        '''Confirma la seleccion e intenta iniciar la partida'''
        try:
            
            # Recibir los campos de configuracion guardados
            filas = int(config_window.entry_filas.get())
            columnas = int(config_window.entry_columnas.get())
            minas = int(config_window.entry_minas.get())

            # Validar la entrada
            if filas <= 0 or columnas <= 0 or minas <= 0:
                messagebox.showerror("Error", "Ingrese valores válidos para Filas, Columnas y Minas.")
            elif minas >= filas * columnas:
                messagebox.showerror("Error", "La cantidad de minas debe ser menor que el tamaño del tablero.")
            else:
                self.iniciar_partida(filas, columnas, minas)
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos para Filas, Columnas y Minas.")

    def iniciar_partida(self, filas:int, columnas:int, minas:int) -> None:
        '''Llama al juego con la configuracion ingresada'''
        self.root.destroy()
        llamada = "python game/game.py " + str(filas) + " " + str(columnas) + " " + str(minas)
        os.system(llamada)

if __name__ == "__main__":
    root = tk.Tk()
    app = Menu(root)
    root.mainloop()
