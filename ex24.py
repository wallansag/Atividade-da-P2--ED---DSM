texto_original = input("Insira um texto ou palavra")
letra_antiga = input("Digite a letra a ser substituida")
letra_nova = input("digite a nova letra")

texto_modificado = texto_original.replace(letra_antiga, letra_nova)

print(texto_original)
print(texto_modificado)