import sys
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
        self.f = 0
        self.h = 0
        self.nivel = 0

    def dar_paso_astar(self, maze):
        """Da los pasos buscando obtaculos, espacios ya ocupados y el final"""
        #   Posiciones actuales
        tablero = maze.tablero
        fila = self.position[0]  # Nodo actual
        columna = self.position[1]
        direcciones = []
        lista_hijos = []
        print("Fila: ", fila, "Columna: ", columna)
        """Revisa arriba"""  # que es lo que tengo que revisar? 1.- Si se salio del borde, y si hay obstruccion
        if fila - 1 >= 0 and tablero[fila - 1][columna] != "#" and tablero[fila - 1][columna] == 0 or tablero[fila - 1][
            columna] == "X":  # si mi fila-1 no se sale del index, ok; y si es diferente de #, ok.
            direcciones.append([fila - 1, columna])
        """Revisa abajo"""
        if fila + 1 <= len(tablero) and tablero[fila + 1][columna] != "#" and tablero[fila + 1][columna] == 0 or \
                tablero[fila + 1][columna] == "X":  # si mi fila+1 no se sale del index, ok; y si es diferente de #, ok.
            direcciones.append([fila + 1, columna])
        """Revisa derecha"""
        if columna + 1 <= len(tablero[fila]) and tablero[fila][columna + 1] != "#" and tablero[fila][
            columna + 1] == 0 or tablero[fila][columna + 1] == "X":
            direcciones.append([fila, columna + 1])
        """Revisa izquierda"""
        if columna - 1 >= 0 and tablero[fila][columna - 1] != "#" and tablero[fila][columna - 1] == 0 or tablero[fila][
            columna - 1] == "X":
            direcciones.append([fila, columna - 1])
        print("Direcciones conseguidas: ", direcciones)
        if direcciones is None:
            return
        for posicion in direcciones:
            print("Direcciones del nodo actual")
            print(posicion)
            hijo = Nodo(None, posicion)
            hijo.funcion_evaluacion(maze)
            hijo.marcar_movimiento(maze.tablero)
            lista_hijos.append(hijo)
        return lista_hijos

    def marcar_movimiento(self, tablero):
        print("ALSJDLAKSD")
        print(tablero[self.position[0]][self.position[1]])
        tablero[self.position[0]][self.position[1]] = int(self.f)

    def funcion_evaluacion(self, maze):
        end = maze.end
        print("\nEn funcion_evaluacion...")
        print("Punto actual: ", self.position)
        print("Punto destino: ", end)
        x_final, x_inicial = end[0], self.position[0]
        y_final, y_inicial = end[1], self.position[1]
        self.h = math.sqrt((x_final - x_inicial) ** 2 + (y_final - y_inicial) ** 2)
        self.f = g + self.h
        print(self.f)

    def camino_de_regres(self, tablero, start, end, lista_cerrada):
        """Esta funcion lo que hara es basicamente ir
           restando para encontrar el camino mas corto. """
        contador = 0
        pos = []
        print("--- En funcion camino_de_regres():")
        process = True
        minimo = tablero[maze.end[0]][maze.end[1]]
        camino = []
        caminos_visitados = []
        opciones = []
        fila_actual = maze.end[0]
        columna_actual = maze.end[1]
        camino.append(maze.end)
        while process:

            """ INICIO PARTE PESADA"""  # Fila[] Columna[]
            """Revisa izquierda"""
            if tablero[fila_actual][columna_actual - 1] != "#":
                if columna_actual - 1 >= 0 and tablero[fila_actual][columna_actual - 1] < tablero[fila_actual][
                    columna_actual] and [fila_actual, columna_actual - 1] not in caminos_visitados:
                    opciones.append([fila_actual, columna_actual - 1])
            print("Valora actual: ", tablero[fila_actual][columna_actual])

            """Revisa arriba"""  # que es lo que tengo que buscar? 1.- Que no se salga del index 2.- El NUMERO anterior
            if tablero[fila_actual - 1][columna_actual] != "#":
                if fila_actual - 1 >= 0 and tablero[fila_actual - 1][columna_actual] < tablero[fila_actual][
                    columna_actual] and [fila_actual - 1, columna_actual] not in caminos_visitados:
                    opciones.append([fila_actual - 1, columna_actual])

            """Revisa abajo"""
            if tablero[fila_actual + 1][columna_actual] != "#":
                if fila_actual + 1 <= len(tablero) and tablero[fila_actual + 1][columna_actual] < tablero[fila_actual][
                    columna_actual] and [fila_actual + 1, columna_actual] not in caminos_visitados:
                    opciones.append([fila_actual + 1, columna_actual])

            """Revisa derecha"""
            if tablero[fila_actual][columna_actual+1] != "#":
                if columna_actual + 1 <= len(tablero[fila_actual]) and tablero[fila_actual][
                    columna_actual + 1] < tablero[fila_actual][columna_actual] and \
                        [fila_actual, columna_actual+1] not in caminos_visitados:
                    opciones.append([fila_actual, columna_actual + 1])

            for i in opciones:
                if minimo > tablero[i[0]][i[1]]:
                    minimo = tablero[i[0]][i[1]]
                    pos = i
            fila_actual = pos[0]
            columna_actual = pos[1]
            if pos not in camino:
                camino.append(pos)
            print("Camino actual: ", camino)
            print("Minimo actual: ", minimo, " en: ", pos)
            print("")

            if [fila_actual, columna_actual] == maze.start:
                camino.append([maze.start[0], maze.start[1]])
                print(opciones)
                print(camino)
                process = False
                return camino

            contador += 1
            if contador == 12:
                print(lista_cerrada)
                sys.exit(0)
            """FIN PARTE PESADA"""


if __name__ == '__main__':
    g = 0
    maze = Maze()
    nodo = Nodo()
    maze.crear_tablero()
    maze.start = [1, 1]
    maze.end = [5, 18]
    maze.ambientar_tablero(maze.start, maze.end)
    maze.imprimir_tablero()
    """En el codigo anterior, se trabajaba con una variable k
    Ahora, se tendria que estar manejando con padres e hijos
    sumandoles la heuristica"""
    # Primero que nada, establecere como se movera y se ira expandiendo el Astar
    nodo.position = maze.start  # El punto inicial del nodo para partir
    nodo.funcion_evaluacion(maze)
    lista_abierta = []
    lista_cerrada = []
    # Ya lo inializamos, ahora solo trabarlo en un while
    lista_abierta.append(nodo)
    print(nodo)
    process = True
    nodo_actual = nodo
    while process:
        if maze.tablero[maze.end[0]][maze.end[1]] != "X":
            print("Camino encontrado!")
            # process = False
            maze.imprimir_tablero()
            nodo_actual.camino_de_regres(maze.tablero, maze.start, maze.end, lista_cerrada)
            break
        lista_hijos = nodo_actual.dar_paso_astar(maze)  # Recibi una lista de hijos en donde a cada uno se le saco la f
        maze.imprimir_tablero()
        for i in lista_hijos: lista_abierta.append(i)  # Se anadio la expansion a la lista abierta
        print("Lista abierta: ")
        for i in lista_abierta:
            print(i)
        lista_abierta.remove(nodo_actual)
        lista_cerrada.append(nodo_actual)
        print("Lista abierta con el actual removido: ")
        for i in lista_abierta:
            print(i, " f:", i.f)
        print("Lista cerrada: ")
        for i in lista_cerrada:
            print(i)
        #   Ahora sigue ordenar la lista de mayor a menor
        contador = 0
        lista_aux = []
        for i in lista_abierta:
            print(contador, ":", i.f)
            lista_aux.append(i.f)
        print("Index valor minimo: ", lista_aux.index(min(lista_aux)))
        index_nodo_menor = lista_aux.index(min(lista_aux))
        nodo_actual = lista_abierta[index_nodo_menor]
        print("Costo actual: ", g)
        g += 1
        """" Aqui seria el final del ciclo"""
