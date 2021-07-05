import matplotlib.pyplot as plt
import copy
import sys

class Maze():
    def __init__(self):
        """Se inicializan las variables"""
        self.start = 0
        self.end = 0
        self.tablero = self.crear_tablero()
        self.tablero_color = []

    def crear_tablero(self):
        tablero = [
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
            [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        return tablero

    def imprimir_tablero(self):
        for i in range(len(self.tablero)):
            for j in range(len(self.tablero[i])):
                print(str(self.tablero[i][j]).ljust(2), end=' ')
            print()

    def ambientar_tablero(self, start, end):
        for i in range(len(self.tablero)):
            for j in range(len(self.tablero[i])):
                if self.tablero[i][j] == 0:
                    self.tablero[i][j] = 0
                if self.tablero[i][j] == 1:
                    self.tablero[i][j] = "#"
        if self.tablero[start[0]][start[1]] == "#":
            print("Escoja otra posicion inicial.")
            sys.exit(0)
        else:
            self.tablero[start[0]][start[1]] = 1
        if self.tablero[end[0]][end[1]] == "#":
            print("Escoja otra posicion inicial.")
            sys.exit(0)
        else:
            self.tablero[end[0]][end[1]] = "X"

    def f(self, inicio, final):
        """Funcion evaluacion"""
        pass
    def h(self, inicio, final):
        """heuristica, costo de movernos entre fichas"""
        pass

    def cambia_un_valor_en_tablero(self, tablero, var_old, var_new):
        for fila in range(len(tablero)):
            for columna in range(len(tablero[fila])):
                if tablero[fila][columna] == var_old:
                    tablero[fila][columna] = var_new
        return tablero

    def colorear_laberinto(self, tablero, start, end, camino):
        """Colorear el laberinto para su prueba final"""
        self.imprimir_tablero()
        print("")
        # Primero cambiar los obstaculos a un numero mas grande
        self.cambia_un_valor_en_tablero(tablero, "#", 80)
        print("Se cambiaron los obstaculos por 80")
        self.imprimir_tablero()
        # Los 0 sobrantes ahora tendran un #
        self.cambia_un_valor_en_tablero(tablero, 0, "#")
        print("\n")
        self.imprimir_tablero()
        print("")
        # Ahora cambiar la ruta
        k = len(camino)
        while len(camino) > 0:
            fila = camino[len(camino)-1][0]
            colu = camino[len(camino)-1][1]
            #print(":", fila, ":", colu) Se imprimen las filas y columnas actuales
            tablero[fila][colu] = 0
            camino.pop()
        self.imprimir_tablero()
        # Ahora cambiar los caminos no escogidos
        for i in range(1,k):
            self.cambia_un_valor_en_tablero(tablero, i, 50)
        self.imprimir_tablero()
        #Por ultimo cambiar los asteriscos
        self.cambia_un_valor_en_tablero(tablero, "#", 5)
        self.imprimir_tablero()
        # y la linea
        self.cambia_un_valor_en_tablero(tablero, 0, 100)
        self.imprimir_tablero()
        plt.matshow(tablero)
        plt.colorbar()
        plt.show()

class Node():
    """Necesitamos una clase nodo para ir trabajando recursivamente"""
    def __init__(self, padre=None, position=None):
        self.padre = padre
        self.position = position
        self.k = 0
        # Funcion evaluacion
        self.g = 0
        self.f = 0
        self.h = 0

    def dar_paso(self, k, tablero, end):
        """Da los pasos buscando el numero, A sus vecinos los denomina con un k+1"""
        for fila in range(len(tablero)):
            for columna in range(len(tablero[fila])):
                if tablero[fila][columna] == k:
                    """Revisa arriba""" # que es lo que tengo que revisar? 1.- Si se salio del borde, y si hay obstruccion
                    if fila-1 >= 0 and tablero[fila-1][columna] != "#" and tablero[fila-1][columna] == 0 or tablero[fila-1][columna] == "X": #si mi fila-1 no se sale del index, ok; y si es diferente de #, ok.
                        tablero[fila - 1][columna] = k+1
                    """Revisa abajo"""
                    if fila+1 <= len(tablero) and tablero[fila+1][columna] != "#" and tablero[fila+1][columna] == 0 or tablero[fila+1][columna] == "X": #si mi fila+1 no se sale del index, ok; y si es diferente de #, ok.
                        tablero[fila + 1][columna] = k+1
                    """Revisa derecha"""
                    if columna+1 <= len(tablero[fila]) and tablero[fila][columna+1] != "#" and tablero[fila][columna+1] == 0 or tablero[fila][columna+1] == "X":
                        tablero[fila][columna+1] = k+1
                    """Revisa izquierda"""
                    if columna - 1 >= 0 and tablero[fila][columna - 1] != "#" and tablero[fila][columna - 1] == 0 or tablero[fila][columna - 1] == "X":
                        tablero[fila][columna - 1] = k + 1
                        # ERROR, NO SOBRESCRIBIR LOS NUMEROS DIFERENTES A 1
        #self.imprimir_tablero(tablero)
        print("Iteracion: ", k)

    def encontrar_camino(self, tablero, end):
        contador = 1
        while tablero[end[0]][end[1]] == "X":
            self.dar_paso(contador, tablero, end)
            contador += 1
        print("Camino encontrado! -------------")
        return contador


    def camino_de_regres(self, tablero, start, end, k):
        """Esta funcion lo que hara es basicamente ir
           restando para encontrar el camino mas corto. """
        print("--- En funcion camino_de_regres():")
        process = True
        next_number = k-1
        camino = []
        lista_aux = []
        print_max = 0
        for item in range(k+1): lista_aux.append(item)
        """Ahora debo empezar a trabar la lista"""
        # Recordando que
        # End son nuestras posiciones finales
        # Start a donde nos dirigimos
        for i in reversed(lista_aux): # Es como la funcion dar paso, va trabando los numeros y sus contiunaciones.
            """Primero una confirmacion para evitar errores"""
            if tablero[end[0]][end[1]] != k:
                print("ERROR 1")
                sys.exit(0)
            else:
                if(print_max == 0 ): print("Valores dentro de la condicional:\n", "\t", "Valor esperado: ", k, "Valor actual: ", tablero[end[0]][end[1]])
                print_max = 1
            # mi posicion initial sera la final al final de cuentas
            fila_actual = end[0]
            columna_actual = end[1]
            while process:
                print(tablero[fila_actual][columna_actual])
                """ INICIO PARTE PESADA""" # Fila[] Columna[]
                """Revisa izquierda"""
                if columna_actual - 1 >= 0 and tablero[fila_actual][columna_actual - 1] == next_number:
                    print("Valor encontrado a la izq")
                    camino.append([fila_actual, columna_actual])  # Anade las coordenadas a una lista llamda camino
                    print(len(camino))  # Lo imprime pa revisar
                    next_number -= 1  # Mi siguiente numero a buscar es el menor proximo
                    columna_actual -= 1  # Mi nueva fila se recorre a la izq, debido a que ahi estaba el siguiente paso
                """Revisa arriba"""  # que es lo que tengo que buscar? 1.- Que no se salga del index 2.- El NUMERO anterior
                if fila_actual-1 >= 0 and tablero[fila_actual-1][columna_actual] == next_number:
                    print("Valor encontrado a la arriba")
                    camino.append([fila_actual, columna_actual])
                    print(len(camino))
                    next_number -= 1
                    fila_actual -= 1
                """Revisa abajo"""
                if fila_actual+1 <= len(tablero) and tablero[fila_actual+1][columna_actual] == next_number:
                    print("Valor encontrado a la abajo")
                    camino.append([fila_actual, columna_actual])
                    print(len(camino))
                    next_number -= 1
                    fila_actual += 1
                """Revisa derecha"""
                if columna_actual+1 <= len(tablero[fila_actual]) and tablero[fila_actual][columna_actual+1] == next_number:
                    print("Valor encontrado a la arriba")
                    camino.append([fila_actual, columna_actual])
                    print(len(camino))
                    next_number -= 1
                    columna_actual += 1

                if(next_number == 0):
                    camino.append([start[0], start[1]])
                    print(camino)
                    process = False
                    return camino
                """FIN PARTE PESADA"""


if __name__ == '__main__':
    nodo = Node()
    maze = Maze()
    """Primero se inicializan los objetos a utilizar"""
    maze.start = 1, 1
    maze.end = 5, 18
    maze.ambientar_tablero(maze.start, maze.end)
    maze.imprimir_tablero()
    print(maze.tablero[0][1])
    print(maze.tablero[1][1])
    nodo.k = nodo.encontrar_camino(maze.tablero, maze.end)
    camino = nodo.camino_de_regres(maze.tablero, maze.start, maze.end, nodo.k)
    maze.imprimir_tablero()
    print(camino)
    tablero_coloredo = copy.deepcopy(maze.tablero)
    maze.tablero_color = copy.deepcopy(maze.tablero)
    maze.colorear_laberinto(maze.tablero_color, maze.start, maze.end, camino)


# tengo que hacer varios pasos para verificar el programa
# Cambios realizados en el Astar