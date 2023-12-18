import tkinter as tk
from .StateIdle import StateIdle

class StateHandlerSingleton:

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.image = tk.PhotoImage()
            cls.__instance.state = None
            cls.__instance.set_state(StateIdle())
            cls.__bombs = 0
        return cls.__instance
    
    def setMapAttributes(self, rows, columns, bombs):
        self.__bombs = bombs
        self.__columns = columns
        self.__rows = rows

    def set_state(self, state):
        if not isinstance(state, type(self.state)):
            self.state = state
            self.execute_state_action()

    def execute_state_action(self):
        self.state.execute(self.change_image)

    def change_image(self, new_image_path):
        self.image = tk.PhotoImage(file=new_image_path)

    def get_image(self):
        return self.image
    
    def getState(self):
        return self.state
    
    def checkWin(self, revealedSpaces):
        return revealedSpaces == self.__rows * self.__columns - self.__bombs - 1