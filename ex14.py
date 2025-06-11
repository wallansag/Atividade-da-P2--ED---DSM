lado1 = int(input("Digite um número para o lado 1"))
lado2 = int(input("Digite um número para o lado 2"))
lado3 = int(input("Digite um número para o lado 3"))

if lado1 == lado2 == lado3:
    print("O triângulo é Equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("O triângulo é Isósceles.")
else:
    print("O triângulo é Escaleno.")