def somar_elementos_lista(lista_numeros):
    """Calcula a soma de todos os elementos em uma lista de números."""
    return sum(lista_numeros)

minha_lista_numeros = [1, 2, 3, 4, 5]
soma_da_lista = somar_elementos_lista(minha_lista_numeros)
print(f"A soma dos elementos da lista {minha_lista_numeros} é: {soma_da_lista}")