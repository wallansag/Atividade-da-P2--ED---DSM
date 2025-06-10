def comprimento_strings(tupla_strings):
    """Recebe uma tupla de strings e retorna uma nova tupla com o comprimento de cada string."""
    return tuple(len(s) for s in tupla_strings)

minha_tupla_strings = ("apple", "banana", "kiwi", "orange")
comprimentos = comprimento_strings(minha_tupla_strings)
print(f"Comprimentos das strings: {comprimentos}")