def aplicar_funcao_lista(lista, funcao):
    
    return [funcao(elemento) for elemento in lista]


def dobrar(x):
    return x * 2

numeros_originais = [1, 2, 3, 4, 5]
numeros_dobrados = aplicar_funcao_lista(numeros_originais, dobrar)
print(numeros_originais)
print(numeros_dobrados)


quadrados = aplicar_funcao_lista(numeros_originais, lambda x: x**2)
print(quadrados)