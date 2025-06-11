def pessoa_mais_velha(lista_pessoas):
   
    if not lista_pessoas:
        return None
    
    mais_velho = lista_pessoas[0]
    for pessoa in lista_pessoas:
        if pessoa[1] > mais_velho[1]:
            mais_velho = pessoa
    return mais_velho

pessoas = [("João", 25), ("José", 30), ("Maria", 22), ("Fulano", 35)]
velho = pessoa_mais_velha(pessoas)
if velho:
    print(f"A pessoa mais velha é: {velho[0]} com {velho[1]} anos.")
else:
    print("A lista de pessoas está vazia.")