from random import shuffle


class Maze:
    def __init__(self):
        self.tablero = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        ]

    def imprimir_tablero(self, tablero):
        for i in range(len(tablero)):
            for j in range(len(tablero[i])):
                print(str(tablero[i][j]).ljust(2), end=' ')
            print()

    def revisa_paso(self, pos_actual, mas):
        if 0 <= pos_actual[0]+mas[0] <= len(self.tablero)-1 and 0 <= pos_actual[1]+mas[1] <= len(self.tablero[0])-1:
            if pos_actual[1] + mas[1] <= len(maze.tablero[0]):
                if self.tablero[pos_actual[0] + mas[0]][pos_actual[1] + mas[1]] == 0:   # Posicion
                    if self.tablero[pos_actual[0] + mas[0]][pos_actual[1] + mas[1]] != "X": # Sin obstaculo
                            self.tablero[pos_actual[0] + mas[0]][pos_actual[1] + mas[1]] = "X"
                            return 1
        return 0

    def maze_bpp(self, position):
        direcciones = [[0, 1], [0, -1], [-1, 0], [1, 0]]  # Derecha, Izquierda, Abajo y Arriba
        # shuffle(direcciones)
        for siguiente in direcciones:
            flag = maze.revisa_paso(position, siguiente)
            maze.paredes
            if flag == 1:
                position[0], position[1] = position[0]+siguiente[0], position[1]+siguiente[1]
                maze.maze_bpp(position)
        print(self.tablero)
        self.imprimir_tablero(self.tablero)



if __name__ == '__main__':
    maze = Maze()
    print("filas: ", len(maze.tablero), "col: ", len(maze.tablero[0]))
    print(5 + (-2))
    start = len(maze.tablero) // 2, len(maze.tablero[0]) // 2
    start = [len(maze.tablero)-1, len(maze.tablero[0])-1]
    maze.tablero[start[0]][start[1]] = "X"
    maze.imprimir_tablero(maze.tablero)
    maze.maze_bpp(start)

