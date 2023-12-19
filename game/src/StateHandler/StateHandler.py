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
            cls.__instance.state = StateIdle()
            cls.__instance.__bombs = 0
            cls.__instance.__interface = None  # Agregamos una variable para almacenar la interfaz
        return cls.__instance
    
    def setMapAttributes(self, rows: int, columns: int, bombs: int) -> None:
        self.__bombs = bombs
        self.__columns = columns
        self.__rows = rows
        self.set_state(StateIdle())

    def set_state(self, state: "GameState") -> None:
        if not isinstance(state, type(self.state)):
            self.state = state
            self.execute_state_action()

    def set_interface(self, interface) -> None:
        '''Establece la interfaz para que el StateHandler pueda interactuar con ella'''
        self.__interface = interface

    def execute_state_action(self, image_path: str) -> None:
        self.change_image(image_path)
        self.__interface.update_interface() if self.__interface else None

    def change_image(self, new_image_path: str) -> None:
        self.image = tk.PhotoImage(file=new_image_path)

    def get_image(self) -> tk.PhotoImage:
        return self.image
    
    def getState(self) -> "GameState.GameState":
        return self.state
    
    def checkWin(self, revealedSpaces: int) -> bool:
        return revealedSpaces == self.__rows * self.__columns - self.__bombs - 1
