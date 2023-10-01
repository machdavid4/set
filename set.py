class ConjuntoUsandoArrayOrdenado:
    def __init__(self):
        self.array = []

    def inserir(self, elemento):
        if elemento not in self.array:
            self.array.append(elemento)
            self.array.sort()

    def remover(self, elemento):
        if elemento in self.array:
            self.array.remove(elemento)

    def contem(self, elemento):
        return elemento in self.array

    def uniao(self, conjunto2):
        novo_conjunto = ConjuntoUsandoArrayOrdenado()
        novo_conjunto.array = list(set(self.array + conjunto2.array))
        novo_conjunto.array.sort()
        return novo_conjunto

    def intersecao(self, conjunto2):
        novo_conjunto = ConjuntoUsandoArrayOrdenado()
        for elemento in self.array:
            if elemento in conjunto2.array:
                novo_conjunto.inserir(elemento)
        return novo_conjunto

    def diferenca(self, conjunto2):
        novo_conjunto = ConjuntoUsandoArrayOrdenado()
        for elemento in self.array:
            if elemento not in conjunto2.array:
                novo_conjunto.inserir(elemento)
        return novo_conjunto

    def obter_elementos(self):
        return self.array

conjunto_set_array_ordenado = ConjuntoUsandoArrayOrdenado()
conjunto_set_array_ordenado.inserir(5)
conjunto_set_array_ordenado.inserir(3)
conjunto_set_array_ordenado.inserir(7)
conjunto_set_array_ordenado.inserir(2)
conjunto_set_array_ordenado.inserir(4)

print("Conjunto Set (Array Ordenado):", conjunto_set_array_ordenado.obter_elementos())

conjunto_set_array_ordenado.remover(3)
print("Apos remover o 3:", conjunto_set_array_ordenado.obter_elementos())

print("Contem o 5:", conjunto_set_array_ordenado.contem(5))
print("Contem o 6:", conjunto_set_array_ordenado.contem(6))

conjunto2_set_array_ordenado = ConjuntoUsandoArrayOrdenado()
conjunto2_set_array_ordenado.inserir(4)
conjunto2_set_array_ordenado.inserir(6)
conjunto2_set_array_ordenado.inserir(8)

print("Uniao:", conjunto_set_array_ordenado.uniao(conjunto2_set_array_ordenado).obter_elementos())
print("Intersecao:", conjunto_set_array_ordenado.intersecao(conjunto2_set_array_ordenado).obter_elementos())
print("Diferenca:", conjunto_set_array_ordenado.diferenca(conjunto2_set_array_ordenado).obter_elementos())