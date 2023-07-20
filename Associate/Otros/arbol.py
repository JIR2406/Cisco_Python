class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if not self.raiz:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(valor, self.raiz)

    def _insertar_recursivo(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierdo:
                self._insertar_recursivo(valor, nodo_actual.izquierdo)
            else:
                nodo_actual.izquierdo = Nodo(valor)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecho:
                self._insertar_recursivo(valor, nodo_actual.derecho)
            else:
                nodo_actual.derecho = Nodo(valor)

    def buscar(self, valor):
        return self._buscar_recursivo(valor, self.raiz)

    def _buscar_recursivo(self, valor, nodo_actual):
        if not nodo_actual:
            return False
        if nodo_actual.valor == valor:
            return True
        elif valor < nodo_actual.valor:
            return self._buscar_recursivo(valor, nodo_actual.izquierdo)
        else:
            return self._buscar_recursivo(valor, nodo_actual.derecho)

    def imprimir_inorden(self):
        elementos = []
        self._imprimir_inorden_recursivo(self.raiz, elementos)
        return elementos

    def _imprimir_inorden_recursivo(self, nodo_actual, elementos):
        if nodo_actual:
            self._imprimir_inorden_recursivo(nodo_actual.izquierdo, elementos)
            elementos.append(nodo_actual.valor)
            self._imprimir_inorden_recursivo(nodo_actual.derecho, elementos)

