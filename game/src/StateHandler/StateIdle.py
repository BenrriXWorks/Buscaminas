from .GameState import GameState

class StateIdle(GameState):
    '''Esta clase define el comportamiento del juego en espera. Extiende a GameState'''

    def execute(self, imageChangeFunction) -> None:
        '''Ejecuta la funcion asociada al estado. Recibe una funcion que consume el path de la nueva imagen'''
        
        print("El juego está en estado Idle.")
        imageChangeFunction('data/restart.png')