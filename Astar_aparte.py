import math
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

class Nodo():
    """Necesitamos una clase nodo para ir trabajando recursivamente"""
    def __init__(self, padre=None, position=None):
        self.padre = padre
        self.position = position
        self.k = 0
        # Funcion evaluacion
        self.g = 0
        self.f = 0
        self.h = 0
        self.nivel = 0

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

    def funcion_evaluacion(self, punto, end):
        x_final, x_inicial = punto[0], punto[1]
        y_final, y_inicial = end[0], end[1]
        print(x_final, x_inicial, "\n", y_final, y_inicial)
        self.h = math.sqrt((x_final - x_inicial) ** 2 + (y_final - y_inicial) ** 2)
        self.g = 1
        self.f = self.g + self.h
        print("Primer heuristica: ", self.f)

if __name__ == '__main__':
    maze = Maze()
    nodo = Nodo()
    maze.crear_tablero()
    maze.start = 1,1
    maze.end = 5,18
    maze.ambientar_tablero(maze.start, maze.end)
    maze.imprimir_tablero()
    """En el codigo anterior, se trabajaba con una variable k
    Ahora, se tendria que estar manejando con padres e hijos
    sumandoles la heuristica"""
    # Primero que nada, establecere como se movera y se ira expandiendo el Astar
    nodo.position = maze.start  # El punto inicial del nodo para partir
    nodo.funcion_evaluacion(nodo.position, maze.end)
