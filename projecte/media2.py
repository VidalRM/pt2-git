def calcular_media(valores):
    suma = sum(valores)
    cantidad_valores = len(valores)
    media = suma / cantidad_valores
    return media

# Ejemplo de uso
valores = [1, 2, 3, 4, 5]
media = calcular_media(valores)
print("La media de la lista de valores es:", media)
