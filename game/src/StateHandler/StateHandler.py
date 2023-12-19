# StateHandler.py
import tkinter as tk
from .StateIdle import StateIdle
from .GameState import GameState

class StateHandlerSingleton:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.image = tk.PhotoImage()
            cls.__instance.state = StateIdle() # Estado base
            cls.__instance.__bombs = 0
        return cls.__instance
    
    def setMapAttributes(self, rows: int, columns: int, bombs: int) -> None:
        '''Coloca los atributos iniciales para calcular la condicion de victoria'''
        self.__bombs = bombs
        self.__columns = columns
        self.__rows = rows
        self.set_state(StateIdle())

    def set_state(self, state: GameState) -> None:
        '''Cambia el estado que maneja el StateHandlerSingleton, para usar su funcion execute'''
        if not isinstance(state, type(self.state)):
            self.state = state
            self.execute_state_action()

    def execute_state_action(self) -> None:
        '''Ejecuta la accion del patron entregado'''
        self.state.execute(self.change_image)

    def change_image(self, new_image_path: str) -> None:
        '''Cambia la imagen que representa el estado de juego para la interfaz'''
        self.image = tk.PhotoImage(file=new_image_path)

    def get_image(self) -> tk.PhotoImage:
        '''Devuelve el objeto de imagen que representa el estado de juego'''
        return self.image
    
    def getState(self) -> GameState:
        '''Devuelve el estado de juego'''
        return self.state
    
    def checkWin(self, revealedSpaces: int) -> bool:
        '''Devuelve true si la cantidad entregada es igual a la cantidad de espacios sin bombas'''
        return revealedSpaces == self.__rows * self.__columns - self.__bombs - 1
