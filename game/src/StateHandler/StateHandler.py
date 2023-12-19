import tkinter as tk
from .StateIdle import StateIdle
from .GameState import GameState

class StateHandlerSingleton:
    '''Esta clase maneja los estados de juego. Es un patron mixto, usando singleton y state'''

    # Instancia singleton
    __instance = None

    def __new__(cls):
        '''Constructor de la clase'''
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.image = tk.PhotoImage()
            cls.__instance.state = None
            cls.__instance.state = StateIdle()
            cls.__bombs = 0
        return cls.__instance
    
    def setMapAttributes(self, rows:int, columns:int, bombs:int) -> None:
        '''Guarda los atributos para calcular si se termino la partida'''
        self.__bombs = bombs
        self.__columns = columns
        self.__rows = rows

    def set_state(self, state:"GameState") -> None:
        '''Cambia el estado de juego'''
        if not isinstance(state, type(self.state)):
            self.state = state
            self.execute_state_action()

    def execute_state_action(self) -> None:
        '''Ejecuta la accion del estado actual'''
        self.state.execute(self.change_image)

    def change_image(self, new_image_path) -> None:
        '''Cambia la imagen del objeto almacenado de imagen'''
        self.image = tk.PhotoImage(file=new_image_path)

    def get_image(self) -> tk.PhotoImage:
        '''Devuelve el objeto imagen que representa al estado'''
        return self.image
    
    def getState(self) -> "GameState.GameState":
        '''Devuelve el estado de juego actual'''
        return self.state
    
    def checkWin(self, revealedSpaces) -> bool:
        '''Retorna true si ya no quedan celdas libres'''
        return revealedSpaces == self.__rows * self.__columns - self.__bombs - 1