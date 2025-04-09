import random

def main():
    print("Selecciona un juego:")
    print("1. N-Reinas")
    print("2. Problema del Caballo")
    print("3. Torres de Hanoi")

    eleccion = input("Ingresa el número del juego: ")

    if eleccion == "1":
        from juegos.reinas.lanzador import resolver_n_reinas
        n = int(input("¿Cuántas reinas?: "))
        soluciones = resolver_n_reinas(n)
        if soluciones:
            print(f"Se encontraron {len(soluciones)} soluciones. Mostrando la primera:")
            solucion = soluciones[0]
            print("Posiciones de las reinas en el tablero:")
            for fila, columna in enumerate(solucion):
                print(f"Reina en fila {fila + 1}, columna {columna + 1}")
        else:
            print("No se encontraron soluciones para el número de reinas proporcionado.")

    elif eleccion == "2":
        from juegos.caballo.lanzador import resolver_caballo
        n = 8  # Tablero fijo de 8x8
        posicion_inicial = (random.randint(0, n - 1), random.randint(0, n - 1))
        print(f"El caballo comienza en la posición: {posicion_inicial}")
        solucion = resolver_caballo(n, posicion_inicial)
        print("Recorrido del caballo:")
        if isinstance(solucion, str):
            print(solucion)
        else:
            for paso, (fila, columna) in enumerate(solucion, start=1):
                print(f"Paso {paso}: El caballo se mueve a la posición ({fila}, {columna})")

    elif eleccion == "3":
        from juegos.hanoi.lanzador import resolver_hanoi
        n = int(input("Cantidad de discos: "))
        movimientos = resolver_hanoi(n)
        print("Secuencia de movimientos:")
        for mov in movimientos:
            print(f"Mover de {mov[0]} a {mov[1]}")

if __name__ == "__main__":
    main()