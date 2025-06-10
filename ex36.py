def aplicar_funcao_lista(lista, funcao):
    """Aplica uma função a cada elemento de uma lista e retorna uma nova lista com os resultados."""
    return [funcao(elemento) for elemento in lista]


def dobrar(x):
    return x * 2

numeros_originais = [1, 2, 3, 4, 5]
numeros_dobrados = aplicar_funcao_lista(numeros_originais, dobrar)
print(f"Lista original: {numeros_originais}")
print(f"Lista com elementos dobrados: {numeros_dobrados}")


quadrados = aplicar_funcao_lista(numeros_originais, lambda x: x**2)
print(f"Lista com elementos ao quadrado: {quadrados}")