def soma_primeiros_n(n):
    """Calcula a soma dos primeiros n números naturais usando range()."""
    return sum(range(1, n + 1))

soma_dos_5 = soma_primeiros_n(5)
print(f"Soma dos primeiros 5 números naturais: {soma_dos_5}")