saldo = 1000.00
saque = float(input("Digite o valor de saque"))

if saque <= saldo:
    saldo -= saque
    print(f"Saque realizado com sucesso.")
    print(f"Novo saldo: R${saldo:.2f}")
else:
    print(f"Saldo insuficiente. {saldo:.2f}.")