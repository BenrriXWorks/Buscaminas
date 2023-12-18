from pygame import mixer
from tkinter import messagebox
import threading

class StateWin:
    def execute(self, imageChangeFunction):
        print("¡Felicidades! Has ganado el juego.")
        imageChangeFunction('data/winIcon.png')

        self.__playVictorySFX()

        messageThread = threading.Thread(target=self.__showVictoryDialog)
        messageThread.daemon = True
        messageThread.start()

    def __playVictorySFX(self) -> None:
        mixer.init()
        mixer.music.load('data/victoria.mp3')
        mixer.music.set_volume(0.7)
        mixer.music.play()

    def __showVictoryDialog(self):
        messagebox.showinfo("Ganaste!", "Despejaste todos los espacios libres, buen trabajo")
        