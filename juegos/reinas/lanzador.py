def resolver_n_reinas(n):
    from juegos.reinas.nodo_reinas import NodoReinas
    from db.database import Session, VectorGuardado  # Importar la sesión y el modelo de la base de datos
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

    # Guardar las soluciones en la base de datos
    session = Session()
    for solucion in soluciones:
        vector_guardado = VectorGuardado(juego="n_reinas", vector={"n": n, "solucion": solucion})
        session.add(vector_guardado)
    session.commit()
    session.close()

    return soluciones

