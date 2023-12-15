from src.Mapa.Mapa import MapaSingleton
import sys
import subprocess


def leerEntrada(entrada):
    '''Recibe un string de la forma ACCION|X,Y. Lo separa y lo interpreta. Ej: $ '''
    return (lambda cmd : ([MapaSingleton.ACCION_MARCAR, MapaSingleton.ACCION_REVELAR][cmd[0] == "R"], \
        map(int, cmd[1].split(",")))) (entrada.split('|'))

def main():

    # Leer los argumentos    
    if (len(sys.argv) != 4):
        print("La llamada al programa es $ ./main.py <rows> <columns> <bombs>")
        return 1
    
    # Crear el mapa
    mapa = MapaSingleton()
    try:
        rows, columns, bombs = map(int, sys.argv[1:])
        mapa.create(rows, columns, bombs)
    except Exception as e:
        print("Entrada invalida")
        print(e)
        return

    accion, x, y = "", 0, 0
    terminar = 0
    # Gameloop
    while True:

        # Realizar la accion declarada anteriormente
        if (accion != ""):
            # Revisar si se termina el juego
            if (mapa.realizarAccion(accion, x, y) == False): terminar = -1
            if (mapa.getRevealedNumber() == rows*columns - bombs): terminar = 1

        # Limpiar la consola e imprimir el mapa
        subprocess.call("cls", shell=True)
        print("💥 B U S C A M I N A S  III 💥")
        mapa.printCeldas()

        # Si el juego se termino, cerrar
        if (terminar == 1): print("Ganaste")
        elif (terminar == -1): print("Perdiste")

        # Leer la entrada
        print("Ejemplo entrada: R|0,0  o  M|1,5")
        entrada = input("Que quieres hacer? (Enter para salir): ").upper()
        if entrada == "": return

        # Interpretar la entrada
        try: accion, (x, y) = leerEntrada(entrada)
        except: continue



if __name__ == "__main__":
    main()