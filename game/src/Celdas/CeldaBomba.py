from .Celda import Celda

class CeldaBomba(Celda):

    def discover(self) -> Celda:
        self.state = Celda.REVEALED
        return self

    def draw(self) -> "Button":
        return '💣'