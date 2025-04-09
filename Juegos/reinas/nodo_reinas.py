from Juegos.base.nodo import Nodo

class NodoReinas(Nodo):
    def __init__(self, estado, n, fila=0, padre=None):
        super().__init__(estado, padre)
        self.n = n
        self.fila = fila

    def es_valido(self, col):
        for i in range(self.fila):
            if self.estado[i] == col or \
               abs(self.estado[i] - col) == self.fila - i:
                return False
        return True

    def generar_hijos(self):
        for col in range(self.n):
            if self.es_valido(col):
                nuevo_estado = self.estado.copy()
                nuevo_estado.append(col)
                hijo = NodoReinas(nuevo_estado, self.n, self.fila + 1, self)
                self.agregar_hijo(hijo)
