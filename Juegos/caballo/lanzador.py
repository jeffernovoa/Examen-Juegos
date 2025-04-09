def resolver_caballo(n=5):
    from juegos.caballo.nodo_caballo import NodoCaballo

    soluciones = []

    def backtrack(nodo):
        if len(nodo.recorrido) == n * n:
            soluciones.append(nodo.recorrido)
            return True
        nodo.generar_hijos()
        for hijo in nodo.hijos:
            if backtrack(hijo):
                return True
        return False

    inicio = (0, 0)
    raiz = NodoCaballo(inicio, [inicio], n)
    backtrack(raiz)
    return soluciones[0] if soluciones else []
