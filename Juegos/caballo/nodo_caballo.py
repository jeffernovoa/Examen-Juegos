from Juegos.base.nodo import Nodo

MOVIMIENTOS = [
    (2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)
]

class NodoCaballo(Nodo):
    def __init__(self, posicion, recorrido, n):
        super().__init__(posicion)
        self.recorrido = recorrido
        self.n = n

    def movimientos_validos(self):
        x, y = self.estado
        for dx, dy in MOVIMIENTOS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.n and 0 <= ny < self.n and (nx, ny) not in self.recorrido:
                yield (nx, ny)

    def generar_hijos(self):
        for movimiento in self.movimientos_validos():
            nuevo_recorrido = self.recorrido + [movimiento]
            hijo = NodoCaballo(movimiento, nuevo_recorrido, self.n)
            self.agregar_hijo(hijo)