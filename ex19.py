try:
    num1 = float(input("Digite um número:  "))
    num2 = float(input("Digite um número: "))
    resultado = num1 / num2
    print(resultado)
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
except ValueError:
    print("Erro: Digite números.")