N = 8

def es_seguro(tablero, fila, col):

    for i in range(col):
        if tablero[fila][i] == 1:
            return False

    i, j = fila, col

    while i >= 0 and j >= 0:
        if tablero[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = fila, col

    while i < N and j >= 0:
        if tablero[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def resolver(tablero, col):

    if col >= N:
        return True

    for fila in range(N):

        if es_seguro(tablero, fila, col):

            tablero[fila][col] = 1

            if resolver(tablero, col + 1):
                return True

            tablero[fila][col] = 0

    return False


tablero = [[0]*N for _ in range(N)]

resolver(tablero, 0)

for fila in tablero:
    print(fila)