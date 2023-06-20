
import csv


def mediana (diccionario):

    valores = []
    for valor in diccionario.values():
        valores.append(valor)

    valores.sort()

    if len(valores)%2 == 0:
        media=(valores[int(len(valores)/2)-1]+valores[int((len(valores)/2))])/2
    else:
        media=valores[int(len(valores)/2)]

    return media

def procesar(nombreFichero, curso):

    estudiantes = []

    try:

        with open(nombreFichero, linea='') as csvfile:
            f = csv.DictReader(csvfile)
            for fila in f:
                if int(fila['Curso']) == curso:
                    estudiantes.append(fila['Nombre'] + ' ' + fila['Apellido'])
        if not estudiantes:
            raise ValueError('No se encuentra el dato')
        

    except ValueError as e:
        return str(e)
    

    return estudiantes

def combinar (diccionario1, diccionario2, diccionario3):
    return


def palabra_repetida(nombreFichero):

    fichero = open(nombreFichero, 'r')
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


#INICIO DEL MAIN (LLAMADAS A FUNCIONES)

#PRIMER EJERCICIO
dic={'v0':5,'v1':3,'v2':8,'v3':1,'v4':6}
print("Valor mediana: ",str(mediana(dic)))

#CUARTO EJERCICIO
ficheroTextoMasRepetidas = 'palabras.txt' #el fichero no lo encuentro en la tarea del examen 
print(palabra_repetida(ficheroTextoMasRepetidas))