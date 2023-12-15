from .Celda import Celda
from .CeldaBomba import CeldaBomba

class CeldaNumero(Celda):

    def discover(self) -> Celda:
        if (self.state == Celda.NON_REVEALED):
            self.state = Celda.REVEALED
            Celda._revealedNumber += 1
            self.value = len(list(filter(lambda n : isinstance(n, CeldaBomba), self.neighbors)))
            if (self.value == 0): 
                for neighbor in self.neighbors:
                    if (neighbor != None and neighbor.state != Celda.REVEALED): 
                        neighbor.discover() 
        return self

    def draw(self) -> "Button":
        return f"{self.value} " if self.value > 0 else "- "