import tkinter as tk
from src.Mapa.Mapa import MapaSingleton
from src.StateHandler.StateHandler import StateHandlerSingleton

rows, columns, bombs = 20, 20, 80

root = tk.Tk()
root.geometry("800x800")

gameStateHandler = StateHandlerSingleton()
gameStateHandler.setMapAttributes(rows, columns, bombs)

mapa = MapaSingleton()
mapa.create(root, rows, columns, bombs)
mapa.pack(fill=tk.BOTH, expand=True)

# Forzar la actualización de la ventana antes de comenzar el bucle principal
root.update()

root.mainloop()