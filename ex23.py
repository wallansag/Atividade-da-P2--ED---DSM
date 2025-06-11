palavra = input("Digite uma palavra")

palavra_invertida = palavra[::-1] 

if palavra == palavra_invertida:
    print(f"É um palíndromo.")
else:
    print(f"não é um palíndromo.")