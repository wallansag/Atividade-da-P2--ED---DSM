def potencias_de_2(expoente_max):
    """Cria uma lista de potências de 2 até um determinado expoente."""
    return [2**i for i in range(expoente_max + 1)]

potencias_ate_4 = potencias_de_2(4)
print(f"Potências de 2 até o expoente 4: {potencias_ate_4}")