def resolver_hanoi(n):
    """
    Resuelve el problema de las Torres de Hanoi para 'n' discos.
    Devuelve una lista de movimientos como tuplas (origen, destino).
    """
    movimientos = []

    def hanoi(discos, origen, auxiliar, destino):
        if discos == 1:
            movimientos.append((origen, destino))
        else:
            hanoi(discos - 1, origen, destino, auxiliar)
            movimientos.append((origen, destino))
            hanoi(discos - 1, auxiliar, origen, destino)

    hanoi(n, 'A', 'B', 'C')
    return movimientos