try:
    num_a = float(input("Digite o primeiro número para divisão: "))
    num_b = float(input("Digite o segundo número para divisão: "))
    resultado_divisao = num_a / num_b
    print(f"Resultado da divisão: {resultado_divisao:.2f}")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite números.")