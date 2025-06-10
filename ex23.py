palavra = "arara" # Tente com "python" para não ser palíndromo

palavra_invertida = palavra[::-1] # Inverte a string

if palavra == palavra_invertida:
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")