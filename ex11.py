num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2


if num2 != 0:
    divisao = num1 / num2
    print(f"Soma: {soma}")
    print(f"Subtração: {subtracao}")
    print(f"Multiplicação: {multiplicacao}")
    print(f"Divisão: {divisao:.2f}")
else:
    print("Soma: {soma}")
    print("Subtração: {subtracao}")
    print("Multiplicação: {multiplicacao}")
    print("Não é possível dividir por zero.")