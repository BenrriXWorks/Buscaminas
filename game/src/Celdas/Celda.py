import abc
import tkinter as tk
from pygame import mixer
from ..StateHandler.StateHandler import StateHandlerSingleton
from ..StateHandler.StateIdle import StateIdle

class Celda(tk.Button, abc.ABC):
    
    # States
    REVEALED = 0
    FLAGGED = 1
    NON_REVEALED = 2

    # Count all revealed cells
    _revealedNumber = 0
    
    # Positions
    TOP_LEFT, TOP, TOP_RIGHT, LEFT, RIGHT, BOTTOM_LEFT, BOTTOM, BOTTOM_RIGHT = range(8)

    # Constructor
    def __init__(self, master=None):

        self.neighbors = [  
            None, None, None,
            None,       None,
            None, None, None
        ]

        self.state = Celda.NON_REVEALED

        super().__init__(master=master, text=self.show(), fg="#464646", bg="#000000", font=('Fixedsys', 18)) # Agregarlo al master
        self.bind("<Button-1>", lambda _ : self.discover()) # Adaptador para descartar el event que devuelve tk
        self.bind("<Button-3>", lambda _ : self.flag())
        # self.bind("<Configure>", lambda _ : self.ajustarFuente())
        
    @abc.abstractmethod
    def discover(self) -> "Celda":
        pass

    @abc.abstractmethod
    def draw(self) -> str:
        pass

    def invertNeighborPos(pos) -> int:
        '''Calcula la posicion opuesta en el arreglo de vecinos'''
        return abs(7 - pos)

    def show(self) -> str:
        if (self.state == Celda.NON_REVEALED):
            return "  "#"⏹️" # Icono de las celdas sin revelar
        if (self.state == Celda.FLAGGED):
            return "🚩"
        if (self.state == Celda.REVEALED):
            return self.draw()

    def addNeighbor(self, neighbor, pos) -> "Celda":
        '''Agrega un vecino a la celda'''
        if (self.neighbors[pos] != None):
            raise ValueError("Se intento agregar un vecino a un espacio no vacio.")
        self.neighbors[pos] = neighbor
        neighbor.neighbors[Celda.invertNeighborPos(pos)] = self

    def flag(self) -> None:
        '''Se marca o desmarca la celda'''
        handler = StateHandlerSingleton()
        if (isinstance(type(handler.getState), StateIdle)):
            if (self.state == Celda.NON_REVEALED):
                self.state = Celda.FLAGGED
                self.configure(fg='red', bg='#350000')
                self.__playFlagSFX()
            elif (self.state == Celda.FLAGGED):
                self.state = Celda.NON_REVEALED
                self.configure(fg='#464646', bg='#000000')
            self.configure(text=self.show())

    def __playFlagSFX(self):
        mixer.init()
        mixer.music.load('data/flag.mp3')
        mixer.music.play()