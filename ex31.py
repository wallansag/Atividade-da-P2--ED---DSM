def gerar_pares(n):
    """Gera uma lista de números pares entre 0 e n."""
    return list(range(0, n + 1, 2))

pares_ate_10 = gerar_pares(10)
print(f"Números pares até 10: {pares_ate_10}")