from ..Celdas.Celda import Celda
from ..Celdas.CeldaBomba import CeldaBomba
from ..Celdas.CeldaNumero import CeldaNumero
import random
import time
from itertools import batched

import tkinter as tk

class MapaSingleton(tk.Frame):
    '''Construye la estructura de las celdas y tiene la funcion para explotar todas las bombas.
    Extiende a Frame.'''

    # Informacion de la clase importante es
    __instance = None
    __firstCellPtr = None

    # Tamaño del mapa
    rows = 0
    columns = 0

    def __new__(cls):
        '''Instance Getter de singleton'''
        if (cls.__instance == None):
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def create(self, master, rows:int, columns:int, bombs:int, *kwargs) -> None:
        '''Construye la red de nodos "Celda" y almacena el puntero al primero.
        Se le debe entregar el master tk para que los nodos sean hijos de ese frame'''

        # Configurar self (frame)
        super().__init__(master=master, bg="lightblue")
        self.grid(sticky="nsew", padx=10, pady=10)
        for row in range(rows): # Que todas las row sean del mismo tamaño
            self.grid_rowconfigure(row, weight=1)
        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)

        # Guardar informacion importante
        self.rows = rows
        self.columns = columns

        # Crear las posiciones con bombas
        self.bombPositions = random.sample([(x,y) for x in range(rows) for y in range(columns)], bombs)

        # Guardar el puntero a la primera celda
        crearCelda = lambda row, column : CeldaNumero(self) if (row, column) not in self.bombPositions else CeldaBomba(self)
        self.__firstCellPtr = crearCelda(0,0)
        self.__firstCellPtr.grid(row=0, column=0, sticky="nsew")

        # Crear la primera fila
        ptr = self.__firstCellPtr
        for row in range(1, rows): 
            newCell = crearCelda(row, 0)
            newCell.grid(row=row, column=0, sticky = "nsew")
            ptr.addNeighbor(newCell, Celda.RIGHT)
            ptr = ptr.neighbors[Celda.RIGHT]
            ptr.grid(row=row, column=0)
        # Crear la primera columna (-1 porque el primer nodo ya esta creado)
        ptr = self.__firstCellPtr
        for column in range(1, columns):
            newCell = crearCelda(0, column)
            newCell.grid(row=0, column=column, sticky = "nsew")
            ptr.addNeighbor(newCell, Celda.BOTTOM)
            ptr = ptr.neighbors[Celda.BOTTOM]
            ptr.grid(row=0, column=column)


        # Crear el resto de la estructura
        columnPtr = self.__firstCellPtr
        for column in range(1, columns):
            
            corner = columnPtr # Vecino de esquina superior izquierda del nodo a crear

            for row in range(1, rows):

                # Crea una nueva celda
                newCell = crearCelda(row, column)
                newCell.grid(row=row, column=column, sticky = "nsew")
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
        
        # Agregar los hermanos de la diagonal de la primera columna (bugfix)
        ptr = columnPtr = self.__firstCellPtr.neighbors[Celda.BOTTOM]
        for _ in range(columns-1):
            rightPtr = ptr.neighbors[Celda.RIGHT]
            if (rightPtr == None): continue
            topRightCornerPtr = rightPtr.neighbors[Celda.TOP]
            ptr.addNeighbor(topRightCornerPtr, Celda.TOP_RIGHT)
            ptr = ptr.neighbors[Celda.BOTTOM]

    def revealAllBombs(self) -> None:
        '''Revela todas las bombas sin descubrir de 10% en 10%'''
        bombasSinDescubrir = list(filter(lambda pos: self.at(pos[0], pos[1]).state == Celda.NON_REVEALED, self.bombPositions))
        for batch in batched(bombasSinDescubrir, max(1, int(len(bombasSinDescubrir)/10))):
            for (x,y) in batch:
                self.at(x,y).discover()
            time.sleep(0.3)

    def at(self, x:int, y:int) -> Celda:
        '''Devuelve la celda en la posicion indicada'''
        if (0 <= x < self.rows and 0 <= y < self.columns):
            ptr = self.__firstCellPtr
            for _ in range(x): ptr = ptr.neighbors[Celda.RIGHT]
            for _ in range(y): ptr = ptr.neighbors[Celda.BOTTOM]
            return ptr
        raise ValueError("Se quiere ingresar a una posicion en el mapa fuera del rango")