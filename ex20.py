string_para_converter = "abc" 

try:
    numero_convertido = int(string_para_converter)
    print(f"A string '{string_para_converter}' foi convertida para o inteiro: {numero_convertido}")
except ValueError:
    print(f"Erro: A string '{string_para_converter}' não pode ser convertida para um número inteiro.")