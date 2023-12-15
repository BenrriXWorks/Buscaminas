import abc

class Celda(abc.ABC):
    
    # States
    REVEALED = 0
    FLAGGED = 1
    NON_REVEALED = 2

    # Count all revealed cells
    _revealedNumber = 0
    
    # Positions
    TOP_LEFT, TOP, TOP_RIGHT, LEFT, RIGHT, BOTTOM_LEFT, BOTTOM, BOTTOM_RIGHT = range(8)

    # Constructor
    def __init__(self):

        self.neighbors = [  
            None, None, None,
            None,       None,
            None, None, None
        ]
        
        self.state = Celda.NON_REVEALED

    @abc.abstractmethod
    def discover(self) -> "Celda":
        pass

    @abc.abstractmethod
    def draw(self) -> "Button":
        pass

    def getRevealedNumber():
        return Celda._revealedNumber

    def invertNeighborPos(pos) -> int:
        '''Calcula la posicion opuesta en el arreglo de vecinos'''
        return abs(7 - pos)

    def show(self) -> 'Button':
        if (self.state == Celda.NON_REVEALED):
            return "⏹️"
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
        if (self.state == Celda.NON_REVEALED):
            self.state = Celda.FLAGGED
        elif (self.state == Celda.FLAGGED):
            self.state = Celda.NON_REVEALED