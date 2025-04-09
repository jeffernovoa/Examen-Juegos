def resolver_hanoi(n):
    from db.database import Session, VectorGuardado  # Importar la sesión y el modelo de la base de datos
    movimientos = []

    def hanoi(discos, origen, auxiliar, destino):
        if discos == 1:
            movimientos.append((origen, destino))
        else:
            hanoi(discos - 1, origen, destino, auxiliar)
            movimientos.append((origen, destino))
            hanoi(discos - 1, auxiliar, origen, destino)

    hanoi(n, 'A', 'B', 'C')

    # Guardar los movimientos en la base de datos
    session = Session()
    vector_guardado = VectorGuardado(juego="hanoi", vector={"n": n, "movimientos": movimientos})
    session.add(vector_guardado)
    session.commit()
    session.close()

    return movimientos