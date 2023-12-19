import abc
import tkinter as tk
from pygame import mixer
from ..StateHandler.StateHandler import StateHandlerSingleton
from ..StateHandler.StateIdle import StateIdle

class Celda(tk.Button, abc.ABC):
    '''Clase abstracta que define a una Celda. Conoce a todos sus vecinos y los tiene en un arreglo. Extiende a tkinter.Button'''

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

        # Crear el Button y vincular los clicks a las funciones
        super().__init__(master=master, text=self.show(), fg="#464646", bg="#000000", font=('Fixedsys', 18)) # Agregarlo al master
        self.bind("<Button-1>", lambda _ : self.discover()) # Adaptador para descartar el event que devuelve tk
        self.bind("<Button-3>", lambda _ : self.flag())
        
    @abc.abstractmethod
    def discover(self) -> "Celda":
        '''Describe el comportamiento de descubrir la celda. Se retorna la misma celda'''
        pass

    @abc.abstractmethod
    def draw(self) -> str:
        '''Devuelve el contenido de string de la celda'''
        pass

    def invertNeighborPos(pos) -> int:
        '''Calcula la posicion opuesta en el arreglo de vecinos'''
        return abs(7 - pos)

    def show(self) -> str:
        '''Devuelve la conversion a str de una celda, tomando en cuenta su estado actual'''
        if (self.state == Celda.NON_REVEALED):
            return "  "
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

        handler = StateHandlerSingleton() # Handler de estado

        # Si el estado no es de victoria ni derrota, se puede seguir marcando
        if isinstance(handler.getState(), StateIdle):
            if (self.state == Celda.NON_REVEALED):
                self.state = Celda.FLAGGED
                self.configure(fg='red', bg='#350000')
                self.__playFlagSFX()
            elif (self.state == Celda.FLAGGED):
                self.state = Celda.NON_REVEALED
                self.configure(fg='#464646', bg='#000000')
            self.configure(text=self.show())

    def __playFlagSFX(self) -> None:
        '''Reproduce el efecto de sonido de colocar una bandera'''
        mixer.init()
        mixer.music.load('data/flag.mp3')
        mixer.music.play()