def mediana(diccionario):
    listaAux = []
    return

def procesar(nombreFichero):
    return

def combinar (diccionario1, diccionario2, diccionario3):
    return


def palabra_repetida(nombre_fichero):
    
    fichero = open(nombre_fichero, 'r')
    palabras = fichero.read().splitlines()
    fichero.close()
    contador_palabras = {}

    for palabra in palabras:
        if palabra in contador_palabras:
            contador_palabras[palabra] += 1
        else:
            contador_palabras[palabra] = 1
    palabra_mas_repetida = ''
    max_repeticiones = 0
    for palabra, repeticiones in contador_palabras.items():
        if repeticiones > max_repeticiones:
            palabra_mas_repetida = palabra
            max_repeticiones = repeticiones
    return palabra_mas_repetida



