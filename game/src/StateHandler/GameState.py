import abc

class GameState(abc.ABC):

    @abc.abstractmethod
    def execute(self):
        '''Ejecuta la accion asociada al estado de juego'''
        pass