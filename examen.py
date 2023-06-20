
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



def procesar (fichero, nCurso):

    f = open(fichero,mode="rt", encoding="utf-8")
    linea = f.readline()

    estudiantes = []

    while linea != "":
        linea = f.readline()
        curso = linea.split(",")[-1]

        if curso[0:1] == str(nCurso):
            estudiantes.append(tuple(linea.split(",")))

    return estudiantes


try:
    lista_estudiantes = procesar("fichero.csv", 2)
    print(lista_estudiantes)
except ValueError as error:
    print("Error:", str(error))
    


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

#SEGUNDO EJERCICIO
ficheroCSV2 = 'alumnos.csv'
print(procesar(ficheroCSV2,3))

#CUARTO EJERCICIO
ficheroTextoMasRepetidas = 'palabras.txt' #el fichero no lo encuentro en la tarea del examen 
print(palabra_repetida(ficheroTextoMasRepetidas))