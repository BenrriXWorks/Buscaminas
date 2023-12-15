from .Celda import Celda

class CeldaVacia(Celda):

    def discover(self) -> "Celda":
        self.state = Celda.REVEALED
        Celda._revealedNumber += 1
        self.neighbors = map(lambda neighbor : neighbor.discover(), self.neighbors)
        return self

    def draw(self) -> "Button":
        return "- "