from ..Celdas.Celda import Celda
from ..Celdas.CeldaBomba import CeldaBomba
from ..Celdas.CeldaNumero import CeldaNumero
import random

class MapaSingleton:

    __instance = None
    __firstCellPtr = None

    # Constantes de ID de accion
    ACCION_REVELAR = 0
    ACCION_MARCAR = 1

    # Tamaño del mapa
    rows = 0
    columns = 0

    def __new__(cls):
        if (cls.__instance == None):
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def create(self, rows, columns, bombs):

        self.rows = rows
        self.columns = columns

        # Crear las posiciones con bombas
        bombPositions = random.sample([(x,y) for x in range(rows) for y in range(columns)], bombs)

        # Guardar el puntero a la primera celda
        crearCelda = lambda row, column : CeldaNumero() if (row, column) not in bombPositions else CeldaBomba()
        self.__firstCellPtr = crearCelda(0,0)

        # Crear la primera fila
        ptr = self.__firstCellPtr
        for row in range(rows-1): 
            ptr.addNeighbor(crearCelda(row, 0), Celda.RIGHT)
            ptr = ptr.neighbors[Celda.RIGHT]
        # Crear la primera columna (-1 porque el primer nodo ya esta creado)
        ptr = self.__firstCellPtr
        for column in range(columns-1):
            ptr.addNeighbor(crearCelda(0, column), Celda.BOTTOM)
            ptr = ptr.neighbors[Celda.BOTTOM]

        # Crear el resto de la estructura
        columnPtr = self.__firstCellPtr
        for column in range(0, columns-1):
            
            corner = columnPtr # Vecino de esquina superior izquierda del nodo a crear

            for row in range(0, rows-1):

                # Crea una nueva celda
                newCell = crearCelda(row+1, column+1)
                ptr = corner

                # Agregar los vecinos Superior, SuperiorIzquierdo, SuperiorDerecho e Izquierdo a la nueva Celda
                ptr.addNeighbor(newCell, Celda.BOTTOM_RIGHT)
                ptr = ptr.neighbors[Celda.RIGHT]
                ptr.addNeighbor(newCell, Celda.BOTTOM)
                ptr = ptr.neighbors[Celda.RIGHT]
                if (ptr != None): 
                    ptr.addNeighbor(newCell, Celda.BOTTOM_LEFT)
                ptr = corner.neighbors[Celda.BOTTOM]
                ptr.addNeighbor(newCell, Celda.RIGHT)

                # Aumentar el desface horizontal
                corner = corner.neighbors[Celda.RIGHT]

            # Aumentar el desface vertical
            columnPtr = columnPtr.neighbors[Celda.BOTTOM]
        
        # Agregar los hermanos de la diagonal de la primera columna
        ptr = columnPtr = self.__firstCellPtr.neighbors[Celda.BOTTOM]
        while (ptr != None):
            rightPtr = ptr.neighbors[Celda.RIGHT]
            if (rightPtr == None): continue
            topRightCornerPtr = rightPtr.neighbors[Celda.TOP]
            ptr.addNeighbor(topRightCornerPtr, Celda.TOP_RIGHT)
            ptr = ptr.neighbors[Celda.BOTTOM]
            

        
    def printCeldas(self):
        # Recorre el arbol K-Ario
        yPtr = self.__firstCellPtr
        while (yPtr != None):
            xPtr = yPtr
            while (xPtr != None):
                print(xPtr.show() + " ", end="")
                xPtr = xPtr.neighbors[Celda.RIGHT]
            
            yPtr = yPtr.neighbors[Celda.BOTTOM]
            print("")

    
    def getRevealedNumber(self):
        return Celda.getRevealedNumber()

    def discover(self, x, y):
        return self.__at(x, y).discover()

    def flag(self, x, y):
        return self.__at(x, y).flag()
    
    def __at(self, x, y):
        ptr = self.__firstCellPtr
        for _ in range(x): ptr = ptr.neighbors[Celda.RIGHT]
        for _ in range(y): ptr = ptr.neighbors[Celda.BOTTOM]
        return ptr


    def realizarAccion(self, accion, x, y) -> bool:
        '''Realiza una accion, devuelve false si descubriste una bomba'''
        if (0 <= x < self.rows and 0 <= y < self.columns):
            # Si se quiere marcar
            if (accion == self.ACCION_MARCAR):
                self.__at(x, y).flag()
                return True
            # Si se quiere revelar
            if (accion == self.ACCION_REVELAR and isinstance(self.discover(x, y), CeldaBomba)):
                return False
        return True