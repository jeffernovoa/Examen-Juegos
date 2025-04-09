def resolver_n_reinas(n):
    from .nodo_reinas import NodoReinas
    soluciones = []

    def backtrack(nodo):
        if len(nodo.estado) == nodo.n:
            soluciones.append(nodo.estado)
            return
        nodo.generar_hijos()
        for hijo in nodo.hijos:
            backtrack(hijo)

    raiz = NodoReinas([], n)
    backtrack(raiz)
    return soluciones

