def medias_coordenadas(lista_coordenadas):
    
    if not lista_coordenadas:
        return (0.0, 0.0) 
    
    soma_x = sum(coord[0] for coord in lista_coordenadas)
    soma_y = sum(coord[1] for coord in lista_coordenadas)
    
    media_x = soma_x / len(lista_coordenadas)
    media_y = soma_y / len(lista_coordenadas)
    
    return (media_x, media_y)

coordenadas = [(1, 2), (3, 4), (5, 6)]
medias = medias_coordenadas(coordenadas)
print(medias)