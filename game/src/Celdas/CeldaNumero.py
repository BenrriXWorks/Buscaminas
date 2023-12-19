from .Celda import Celda
from .CeldaBomba import CeldaBomba

from ..StateHandler.StateHandler import StateHandlerSingleton
from ..StateHandler.StateIdle import StateIdle
from ..StateHandler.StateWin import StateWin

from pygame import mixer

class CeldaNumero(Celda):
    '''Esta clase define una celda de tipo numero. Extiende a Celda'''

    # Colores de los numeros
    __numberColors = ['#F5F5F5', '#2196F3', '#4CAF50', '#F44336', '#FFC107', '#9C27B0', '#FF5722', '#795548', '#607D8B']

    def __init__(self, master=None):
        '''Constructor de CeldaNumero. Se le puede indicar el master para que sea hijo de ese frame'''
        super().__init__(master)

    def discover(self) -> Celda:
        '''Descubre la celda si no esta descubierta, ni marcada, y estamos en un estado valido. La devuelve'''

        gameState = StateHandlerSingleton()

        if (self.state == Celda.NON_REVEALED 
            and isinstance(gameState.getState(), StateIdle)):

            self.__playDiscoverSFX()

            # Cambiar el estado de juego a victoria si se gano
            if gameState.checkWin(self._revealedNumber): gameState.set_state(StateWin())

            self.state = Celda.REVEALED
            Celda._revealedNumber += 1
            self.value = len(list(filter(lambda n : isinstance(n, CeldaBomba), self.neighbors)))
            self.configure(text=self.draw(), bg='#262626', fg=self.__numberColors[self.value])
            if (self.value == 0): 
                self.configure(bg="#444444")
                for neighbor in self.neighbors:
                    if (neighbor != None and neighbor.state != Celda.REVEALED): 
                        neighbor.discover() 

        return self

    def draw(self) -> str:
        ''''Devuelve el contenido str de la celda'''
        return f"{self.value} " if self.value > 0 else "  "
    
    def __playDiscoverSFX(self) -> None:
        '''Reproduce el efecto de sonido de descubrir una celda'''
        mixer.init()
        mixer.music.load('data/beep.mp3')
        mixer.music.play()