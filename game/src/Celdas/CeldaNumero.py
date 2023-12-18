from .Celda import Celda
from .CeldaBomba import CeldaBomba

from ..StateHandler.StateHandler import StateHandlerSingleton
from ..StateHandler.StateIdle import StateIdle
from ..StateHandler.StateWin import StateWin

from pygame import mixer

class CeldaNumero(Celda):

    __numberColors = ['#F5F5F5', '#2196F3', '#4CAF50', '#F44336', '#FFC107', '#9C27B0', '#FF5722', '#795548', '#607D8B']

    def __init__(self, master):
        super().__init__(master)

    def discover(self) -> Celda:

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
        return f"{self.value} " if self.value > 0 else "  "
    
    def __playDiscoverSFX(self):
        mixer.init()
        mixer.music.load('data/beep.mp3')
        mixer.music.play()