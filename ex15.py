saldo = 1000.00
valor_saque = 300.00

if valor_saque <= saldo:
    saldo -= valor_saque
    print(f"Saque de R${valor_saque:.2f} realizado com sucesso.")
    print(f"Novo saldo: R${saldo:.2f}")
else:
    print(f"Saldo insuficiente. Seu saldo atual é de R${saldo:.2f}.")