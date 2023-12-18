from .Celda import Celda
import threading
import time
import tkinter as tk

class CeldaBomba(Celda):

    def discover(self) -> Celda:
        if (self.state == Celda.NON_REVEALED):
            
            self.state = Celda.REVEALED

            self.configure(text=self.draw(), fg="white")
            thread = threading.Thread(target=lambda : self.__explodingColors(0))
            thread.daemon = True
            thread.start()
        return self

    def draw(self) -> str:
        return '💣'
    
    def __explodingColors(self, i) -> None:

        time.sleep(0.3)
        self.configure(bg=['#FF8717','#FF2C5D'][i%2 == 0])
        self.__explodingColors(i+1)