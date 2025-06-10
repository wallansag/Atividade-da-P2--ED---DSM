lista_com_duplicados = [1, 2, 2, 3, 4, 4, 5, 1]
lista_sem_duplicados = list(set(lista_com_duplicados)) # Converte para set (remove duplicados) e volta para lista

print(f"Lista com duplicados: {lista_com_duplicados}")
print(f"Lista sem duplicados: {lista_sem_duplicados}")