import tkinter as tk
from src.Mapa.Mapa import MapaSingleton

root = tk.Tk()
root.geometry("800x800")

mapa = MapaSingleton()
mapa.create(root, 40, 40, 100)
mapa.pack(fill=tk.BOTH, expand=True)

# Forzar la actualización de la ventana antes de comenzar el bucle principal
root.update()

root.mainloop()