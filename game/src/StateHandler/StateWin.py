from .GameState import GameState
from pygame import mixer
from tkinter import messagebox
import threading

class StateWin(GameState):
    '''Esta clase define el comportamiento del estado de victoria. Extiende a GameState.'''
    
    def execute(self, imageChangeFunction) -> None:
        '''Ejecuta la accion asociada al estado'''
        print("¡Felicidades! Has ganado el juego.")
        imageChangeFunction('data/winIcon.png')

        self.__playVictorySFX() # Sonido de victoria

        # Thread para mensaje de victoria
        messageThread = threading.Thread(target=self.__showVictoryDialog)
        messageThread.daemon = True
        messageThread.start()

    def __playVictorySFX(self) -> None:
        '''Hace sonar el sfx de victoria'''
        mixer.init()
        mixer.music.load('data/victoria.mp3')
        mixer.music.set_volume(0.7)
        mixer.music.play()

    def __showVictoryDialog(self) -> None:
        '''Muestra el dialogo de victoria'''
        messagebox.showinfo("Ganaste!", "Despejaste todos los espacios libres, buen trabajo")
        