def fibonacci(n):
    
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

termo_fibonacci = int(input("Digite um termo"))
print(f"O {termo_fibonacci}º termo é: {fibonacci(termo_fibonacci)}")