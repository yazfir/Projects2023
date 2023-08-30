import json
from io import *

def crearArchivo(nombre, contenido):
    archivo = open(nombre,"a")
    archivo.write(contenido)
    archivo.close()

def leeArchivo(nombre):
    archivo = open(nombre,"r")
    cadena = archivo.read()
    archivo.close()
    return cadena

def ejercicio1():
    #Crear un dict con autores y titulos de libros. Convertirlos a formato Json y
    #almacenarlos en un archivo
    libros={
        'libro1':'autor1',
        'libro2':'autor2',
        'libro3':'autor3',
        'libro4':'autor2',
        'libro5':'autor1',
    }

    libjson = json.dumps(libros)
    crearArchivo('librosJson.txt',libjson)

def ejercicio2():
    #Dado un archivo Json de Directores y Titulos de Peliculas, leerlo y convertirlo a dict
    #con ese dict, crear una lista de directores y otra de peliculas

    infoDyM = leeArchivo("dirymovies.txt")

    dictDyM = json.loads(infoDyM)

    print(dictDyM)

    print(dictDyM.keys())
    print(dictDyM.values())


#ejercicio1()
ejercicio2()