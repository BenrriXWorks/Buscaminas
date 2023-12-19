from .Celda import Celda
import threading
import time
import tkinter as tk
from ..StateHandler.StateHandler import StateHandlerSingleton
from ..StateHandler.StateLose import StateLose
from ..StateHandler.StateWin import StateWin

from pygame import mixer

class CeldaBomba(Celda):
    '''Esta celda describe una celda de tipo Bomba. Extiende a Celda'''

    def discover(self) -> Celda:
        if (self.state == Celda.NON_REVEALED):

            handler = StateHandlerSingleton() # El handler del estado de juego

            # Si no hay victoria, aun se pueden pulsar las bombas
            if not (isinstance(handler.getState(), StateWin)):
                    
                self.state = Celda.REVEALED
                handler.set_state(StateLose())

                # Hacer el thread con la funcion de cambiar de color
                self.configure(text=self.draw(), fg="white")
                thread = threading.Thread(target=self.__explodingColors)
                thread.daemon = True
                thread.start()

        return self

    def draw(self) -> str:
        '''Devuelve la conversion a str de la celda'''
        return '💣'
    
    def __explodingColors(self) -> None:
        '''Hace que la celda cambie de colores'''
        # Primero reproduce el sonido
        self.__playExplosionSFX()
        # Mantiene a la celda cambiando de colores
        i = 0
        while True:
            self.configure(bg=['#FF8717','#FF2C5D'][i%2 == 0])
            i += 1
            time.sleep(0.3)

    def __playExplosionSFX(self) -> None:
        '''Reproduce el sonido de explosion al descubrir una bomba'''
        mixer.init()
        mixer.music.load('data/explosionAlt.mp3')
        mixer.music.set_volume(0.7)
        mixer.music.play()