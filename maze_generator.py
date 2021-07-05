import sys
from random import shuffle


class Maze:
    def __init__(self):
        self.tablero = [
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        self.end = []
        self.start = []

    def imprimir_tablero(self, tablero):
        for i in range(len(tablero)):
            for j in range(len(tablero[i])):
                print(str(tablero[i][j]).ljust(2), end=' ')
            print()

    def revisa_paso(self, pos_actual, sig):
        fila = pos_actual[0] + sig[0]
        columna = pos_actual[1] + sig[1]
        tablero = self.tablero
        """Revisa arriba"""  # que es lo que tengo que revisar? 1.- Si se salio del borde, y si hay obstruccion
        if fila - 1 >= 0 and tablero[fila - 1][columna] != "#" and tablero[fila - 1][columna] == 0 or tablero[fila - 1][
            columna] == "X":  # si mi fila-1 no se sale del index, ok; y si es diferente de #, ok.
            tablero[fila - 1][columna] = 1
            return 1
        """Revisa abajo"""
        if fila + 1 <= len(tablero) and tablero[fila + 1][columna] != "#" and tablero[fila + 1][columna] == 0 or \
                tablero[fila + 1][columna] == "X":  # si mi fila+1 no se sale del index, ok; y si es diferente de #, ok.
            tablero[fila + 1][columna] = 1
            return 1
        """Revisa derecha"""
        if columna + 1 <= len(tablero[fila]) and tablero[fila][columna + 1] != "#" and tablero[fila][
            columna + 1] == 0 or tablero[fila][columna + 1] == "X":
            tablero[fila][columna+1] = 1
            return 1
        """Revisa izquierda"""
        if columna - 1 >= 0 and tablero[fila][columna - 1] != "#" and tablero[fila][columna - 1] == 0 or tablero[fila][
            columna - 1] == "X":
            tablero[fila + 1][columna-1] = 1
            return 1

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

    def maze_bpp(self, position):
        direcciones = [[0, 1], [0, -1], [-1, 0], [1, 0]]  # Derecha, Izquierda, Abajo y Arriba
        # shuffle(direcciones)
        for siguiente in direcciones:
            print(position)
            print(siguiente)
            flag = maze.revisa_paso(position, siguiente)
            self.imprimir_tablero(self.tablero)
            print("")
            if flag == 1:
                maze.maze_bpp(position)





if __name__ == '__main__':
    maze = Maze()
    print("filas: ", len(maze.tablero), "col: ", len(maze.tablero[0]))
    print(5 + (-2))
    maze.start = [1,1]
    maze.end = [5,18]
    maze.ambientar_tablero(maze.start, maze.end)
    maze.imprimir_tablero(maze.tablero)
    maze.maze_bpp(maze.start)