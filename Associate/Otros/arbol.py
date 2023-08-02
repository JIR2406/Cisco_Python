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

    def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(valor, self.raiz)

    def _eliminar_recursivo(self, valor, nodo_actual):
        if not nodo_actual:
            return nodo_actual

        if valor < nodo_actual.valor:
            nodo_actual.izquierdo = self._eliminar_recursivo(valor, nodo_actual.izquierdo)
        elif valor > nodo_actual.valor:
            nodo_actual.derecho = self._eliminar_recursivo(valor, nodo_actual.derecho)
        else:
            # Caso 1: El nodo a eliminar es una hoja (no tiene hijos)
            if not nodo_actual.izquierdo and not nodo_actual.derecho:
                nodo_actual = None
            # Caso 2: El nodo a eliminar tiene solo un hijo (derecho)
            elif not nodo_actual.izquierdo:
                nodo_actual = nodo_actual.derecho
            # Caso 3: El nodo a eliminar tiene solo un hijo (izquierdo)
            elif not nodo_actual.derecho:
                nodo_actual = nodo_actual.izquierdo
            # Caso 4: El nodo a eliminar tiene dos hijos
            else:
                # En este caso, buscamos el sucesor inorden del nodo a eliminar
                # (el menor nodo en el subárbol derecho) y lo reemplazamos
                sucesor = self._encontrar_minimo(nodo_actual.derecho)
                nodo_actual.valor = sucesor.valor
                # Luego, eliminamos el sucesor del subárbol derecho
                nodo_actual.derecho = self._eliminar_recursivo(sucesor.valor, nodo_actual.derecho)

        return nodo_actual

    def _encontrar_minimo(self, nodo_actual):
        if not nodo_actual.izquierdo:
            return nodo_actual
        return self._encontrar_minimo(nodo_actual.izquierdo)
    
    def eliminar_todo(self):
        self.raiz = None