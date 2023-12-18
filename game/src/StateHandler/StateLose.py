import threading
from tkinter import messagebox

class StateLose:
    def execute(self, imageChangeFunction):
        print("Lo siento, has perdido el juego.")
        imageChangeFunction('data/bombIcon.png')

        thread = threading.Thread(target=self.__explodeBombs)
        thread.daemon = True
        thread.start()

        messageThread = threading.Thread(target=self.__showLoseDialog)
        messageThread.daemon = True
        messageThread.start()
        

    def __explodeBombs(self):
        from ..Mapa.Mapa import MapaSingleton # Resuelve el import circular :)
        mapa = MapaSingleton()
        mapa.revealAllBombs()
    
    def __showLoseDialog(self):
        messagebox.showerror("Boom!", "Has perdido el juego") # Ventanita de informacion