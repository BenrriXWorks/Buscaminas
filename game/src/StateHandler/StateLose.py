from .GameState import GameState
import threading
from tkinter import messagebox

class StateLose(GameState):
    '''Esta clase define el comportamiento del estado de derrota. Extiende GameState.'''

    def execute(self, imageChangeFunction) -> None:
        '''Ejecuta la funcion asociada al estado
            args: 
                1) imageChangeFunction(path): Funcion que recibe el path de la nueva imagen para cambiarse 
        '''

        print("Lo siento, has perdido el juego.")
        imageChangeFunction('data/bombIcon.png')

        thread = threading.Thread(target=self.__explodeBombs)
        thread.daemon = True
        thread.start()

        messageThread = threading.Thread(target=self.__showLoseDialog)
        messageThread.daemon = True
        messageThread.start()
        

    def __explodeBombs(self) -> None:
        '''Indica al mapa explotar todas las bombas'''
        from ..Mapa.Mapa import MapaSingleton # Resuelve el import circular :)
        mapa = MapaSingleton()
        mapa.revealAllBombs()
    
    def __showLoseDialog(self) -> None:
        '''Muestra el mensaje de derrota'''
        messagebox.showerror("Boom!", "Has perdido el juego") # Ventanita de informacion