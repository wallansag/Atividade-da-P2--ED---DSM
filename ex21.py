nome_arquivo = "arquivo_inexistente.txt" 

try:
    with open(nome_arquivo, 'r') as f:
        conteudo = f.read()
        print(f"Conteúdo do arquivo '{nome_arquivo}':\n{conteudo}")
except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")