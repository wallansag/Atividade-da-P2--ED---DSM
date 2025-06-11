string = input("Digite um número")

try:
    numero = int(string)
    print(string)
except ValueError:
    print(f"Erro: A string  não pode ser convertida para um número inteiro.")