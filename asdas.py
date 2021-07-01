def go_to(i, j):
    global camino1, end_i, end_j, lab , m
    if i < 0 or j < 0 or i > len(lab)-1 or j > len(lab[0])-1:
        return
    # si ya hemos estado aqui o hay un muro pues agregar a la lista de camino1
    if (i, j) in camino1 or lab[i][j] > 0:
        return
    camino1.append((i, j))
    lab[i][j] = 2
    #print_lab(lab)
    #aqui generar tamvien un print de la lab

    if (i, j) == (end_i, end_j):
        print("Camino a seguir: ")
        print(" ")
        print(camino1)
        camino1.pop()
        return
    else:
        go_to(i - 1, j)  # arriba
        go_to(i + 1, j)  # abajo
        go_to(i, j + 1)  # derecha
        go_to(i, j - 1)  # izquierda
    camino1.pop()

    return

#aca enviamos al metodo la posicion inicial y la posicion final
go_to(start_i, start_j)