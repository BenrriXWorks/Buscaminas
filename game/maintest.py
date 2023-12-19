import tkinter as tk
from src.Mapa.Mapa import MapaSingleton
from src.StateHandler.StateHandler import StateHandlerSingleton
import sys

class Main:

    def main():

        # Leer los argumentos
        try:
            if (len(sys.argv) != 4):
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

        # Crear el mapa de celdas
        mapa = MapaSingleton()
        mapa.create(root, rows, columns, bombs)
        mapa.pack(fill=tk.BOTH, expand=True)

        # Iniciar el loop de renderizado de tkinter
        root.mainloop()

if __name__ == "__main__":

    Main.main()