def resolver_caballo(n, posicion_inicial):
    from db.database import Session, VectorGuardado  # Importar la sesión y el modelo de la base de datos
    movimientos = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]
    tablero = [[-1 for _ in range(n)] for _ in range(n)]
    fila_inicial, columna_inicial = posicion_inicial
    tablero[fila_inicial][columna_inicial] = 0

    def mover_caballo(fila, columna, paso):
        if paso == n * n:
            return True
        for mov in movimientos:
            nueva_fila = fila + mov[0]
            nueva_columna = columna + mov[1]
            if 0 <= nueva_fila < n and 0 <= nueva_columna < n and tablero[nueva_fila][nueva_columna] == -1:
                tablero[nueva_fila][nueva_columna] = paso
                if mover_caballo(nueva_fila, nueva_columna, paso + 1):
                    return True
                tablero[nueva_fila][nueva_columna] = -1  # Retroceso
        return False

    if not mover_caballo(fila_inicial, columna_inicial, 1):
        return "No se encontró un recorrido válido."

    # Convertir el tablero en una lista de movimientos
    recorrido = []
    for paso in range(n * n):
        for fila in range(n):
            for columna in range(n):
                if tablero[fila][columna] == paso:
                    recorrido.append((fila, columna))

    # Guardar el recorrido en la base de datos
    session = Session()
    vector_guardado = VectorGuardado(juego="caballo", vector={"n": n, "inicio": posicion_inicial, "recorrido": recorrido})
    session.add(vector_guardado)
    session.commit()
    session.close()

    return recorrido
