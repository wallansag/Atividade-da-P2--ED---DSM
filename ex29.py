def medias_coordenadas(lista_coordenadas):
    """Converte uma lista de coordenadas (x, y) em uma tupla contendo as médias de x e y."""
    if not lista_coordenadas:
        return (0.0, 0.0) # Retorna (0,0) ou pode levantar um erro
    
    soma_x = sum(coord[0] for coord in lista_coordenadas)
    soma_y = sum(coord[1] for coord in lista_coordenadas)
    
    media_x = soma_x / len(lista_coordenadas)
    media_y = soma_y / len(lista_coordenadas)
    
    return (media_x, media_y)

coordenadas = [(1, 2), (3, 4), (5, 6)]
medias = medias_coordenadas(coordenadas)
print(f"Médias das coordenadas: {medias}")