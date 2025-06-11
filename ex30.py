def comprimento_strings(tupla_strings):
   
    return tuple(len(s) for s in tupla_strings)

minha_tupla_strings = ("apple", "banana", "kiwi", "orange")
comprimentos = comprimento_strings(minha_tupla_strings)
print(f"Comprimentos das strings: {comprimentos}")