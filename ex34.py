def fibonacci(n):
    """Calcula o n-ésimo termo da sequência de Fibonacci de forma recursiva."""
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

termo_fibonacci = 7
print(f"O {termo_fibonacci}º termo da sequência de Fibonacci é: {fibonacci(termo_fibonacci)}")