class Maze():
    def __init__(self):
        self.tablero = [
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


class Node(Maze):
    """Necesitamos una clase nodo para ir trabajando recursivamente"""
    def __init__(self, padre=None, position=None):
        super().__init__()
        self.padre = padre
        self.position = position
        # Funcion evaluacion
        self.g = 0
        self.f = 0
        self.h = 0

    def __eq__(self, other):
        return self.position == other.position

if __name__ == '__main__':
    nodo = Node()
    start = 1,1
    end = 5,18
    nodo.ambientar_tablero(start,end)
    nodo.imprimir_tablero()