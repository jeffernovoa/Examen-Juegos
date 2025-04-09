class Nodo:
    def __init__(self, estado, padre=None):
        self.estado = estado
        self.padre = padre
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)
