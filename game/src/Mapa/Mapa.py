from ..Celdas.Celda import Celda
from ..Celdas.CeldaBomba import CeldaBomba
from ..Celdas.CeldaNumero import CeldaNumero
import random

class MapaSingleton:

    __instance = None
    __mapa = []

    # Constantes de ID de accion
    ACCION_REVELAR = 0
    ACCION_MARCAR = 1

    def __new__(cls):
        if (cls.__instance == None):
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def create(self, rows, columns, bombs):

        self.rows = rows
        self.columns = columns

        # Crear las posiciones con bombas
        bombPositions = random.sample([(x,y) for x in range(rows) for y in range(columns)], bombs)

        # Generar el __mapa
        for column in range(columns):
            self.__mapa.append([])
            for row in range(rows):
                newCell = CeldaNumero() if (row, column) not in bombPositions else CeldaBomba()
                if (row > 0): newCell.addNeighbor(self.__mapa[column][row-1], Celda.LEFT)
                if (column > 0): newCell.addNeighbor(self.__mapa[column-1][row], Celda.TOP)
                if (row > 0 and column > 0): newCell.addNeighbor(self.__mapa[column-1][row-1], Celda.TOP_LEFT)
                if (row + 1 < rows and column > 0): newCell.addNeighbor(self.__mapa[column-1][row+1], Celda.TOP_RIGHT)
                self.__mapa[column].append(newCell)
        
    def printCeldas(self):
        # firstCell = self.__mapa[0][0]
        for row in self.__mapa:
            str = " ".join(map(lambda x : x.show(), row))
            print(str)
    
    def getRevealedNumber(self):
        return Celda.getRevealedNumber()

    def discover(self, x, y):
        return self.__mapa[y][x].discover()

    def flag(self, x, y):
        return self.__mapa[y][x].flag()

    def realizarAccion(self, accion, x, y) -> bool:
        '''Realiza una accion, devuelve false si descubriste una bomba'''
        if (0 <= x < self.rows and 0 <= y < self.columns):
            # Si se quiere marcar
            if (accion == self.ACCION_MARCAR):
                self.__mapa[y][x].flag()
                return True
            # Si se quiere revelar
            if (accion == self.ACCION_REVELAR and isinstance(self.discover(x, y), CeldaBomba)):
                return False
        return True