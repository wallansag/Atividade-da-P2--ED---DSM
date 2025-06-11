arquivo = "arquivo1.txt" 

try:
    with open(arquivo, 'r') as f:
        conteudo = f.read()
        print(f"Conteúdo do arquivo '{arquivo}':\n{conteudo}")
except FileNotFoundError:
    print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")