from juegos.base.nodo import Nodo

class NodoHanoi(Nodo):
    def __init__(self, torres, padre=None):
        super().__init__(torres, padre)

    def mover(self, origen, destino):
        nuevo = [list(t) for t in self.estado]
        disco = nuevo[origen].pop()
        nuevo[destino].append(disco)
        return NodoHanoi(nuevo, self)

    def generar_hijos(self):
        for i in range(3):
            if not self.estado[i]:
                continue
            for j in range(3):
                if i != j and (not self.estado[j] or self.estado[i][-1] < self.estado[j][-1]):
                    self.agregar_hijo(self.mover(i, j))
