def elementos_comuns(lista1, lista2):
    
    return list(set(lista1) & set(lista2)) 

lista_a = [1, 2, 3, 4, 5]
lista_b = [4, 5, 6, 7, 8]
comuns = elementos_comuns(lista_a, lista_b)
print(f"Elementos comuns entre {lista_a} e {lista_b}: {comuns}")