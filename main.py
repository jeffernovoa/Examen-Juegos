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
        print(f"Se encontraron {len(soluciones)} soluciones. Mostrando la primera:")
        print(soluciones[0])

    elif eleccion == "2":
        from juegos.caballo.lanzador import resolver_caballo
        n = int(input("Tamaño del tablero NxN: "))
        solucion = resolver_caballo(n)
        print("Recorrido del caballo:")
        print(solucion)

    elif eleccion == "3":
        from juegos.hanoi.lanzador import resolver_hanoi
        n = int(input("Cantidad de discos: "))
        movimientos = resolver_hanoi(n)
        print("Secuencia de movimientos:")
        for mov in movimientos:
            print(f"Mover de {mov[0]} a {mov[1]}")

if __name__ == "__main__":
    main()
