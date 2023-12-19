import tkinter as tk
from Interfaz import Interfaz
from src.StateHandler.StateHandler import StateHandlerSingleton
import sys

class Main:

    @staticmethod
    def main():
        # Leer los argumentos
        try:
            if len(sys.argv) != 4:
                raise ValueError("La llamada debe ser $ game.py <filas> <columnas> <bombas>")
            rows, columns, bombs = map(int, sys.argv[1:])
        except Exception as e:
            print("Hubo un error:", e)
            return

        # Crear la ventana
        root = tk.Tk()
        root.geometry("800x800")

        # Iniciar el manejador del estado de juego
        gameStateHandler = StateHandlerSingleton()
        gameStateHandler.setMapAttributes(rows, columns, bombs)

        # Crear la interfaz
        interfaz = Interfaz(root)
        interfaz.inicializar_interfaz(rows, columns, bombs)  # Ajusta según la interfaz

        # Iniciar el loop de renderizado de tkinter
        root.mainloop()

if __name__ == "__main__":
    Main.main()
