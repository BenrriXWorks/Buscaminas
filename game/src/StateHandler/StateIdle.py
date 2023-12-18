
class StateIdle:
    def execute(self, imageChangeFunction):
        print("El juego está en estado Idle.")
        imageChangeFunction('data/restart.png')