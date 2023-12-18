from .Celda import Celda
from .CeldaBomba import CeldaBomba

class CeldaNumero(Celda):

    __numberColors = ['#F5F5F5', '#2196F3', '#4CAF50', '#F44336', '#FFC107', '#9C27B0', '#FF5722', '#795548', '#607D8B']

    def __init__(self, master):
        super().__init__(master)

    def discover(self) -> Celda:
        if (self.state == Celda.NON_REVEALED):
            self.state = Celda.REVEALED
            Celda._revealedNumber += 1
            self.value = len(list(filter(lambda n : isinstance(n, CeldaBomba), self.neighbors)))
            self.configure(text=self.draw(), bg='#262626', fg=self.__numberColors[self.value])
            if (self.value == 0): 
                # self.grid_forget() # Se hace transparente
                self.configure(bg="#111111")
                for neighbor in self.neighbors:
                    if (neighbor != None and neighbor.state != Celda.REVEALED): 
                        neighbor.discover() 
        return self

    def draw(self) -> str:
        return f"{self.value} " if self.value > 0 else "  "