import tkinter as tk
from src.StateHandler.StateHandler import StateHandlerSingleton
from src.Mapa.Mapa import MapaSingleton
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
        root.title("💥 B U S C A M I N A S 💥")

        # Crear el mapa
        mapa = MapaSingleton()
        mapa.create(root, rows, columns, bombs)

        # Iniciar el manejador del estado de juego
        gameStateHandler = StateHandlerSingleton()
        gameStateHandler.setMapAttributes(rows, columns, bombs)

        # Agrandar el mapa para que ocupe la pantalla
        mapa.pack()
        mapa.pack(fill=tk.BOTH, expand=True)

        # Iniciar el loop de renderizado de tkinter
        root.mainloop()

if __name__ == "__main__":
    Main.main()
