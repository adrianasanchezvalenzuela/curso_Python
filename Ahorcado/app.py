'''
Programa principal del juego del ahorcado
'''
import os
import unicodedata
import funciones as fn
from random import choice
import string
import argparse

def main(archivo_texto:str, nombre_plantilla='plantilla'):
    '''
    Programa principal del juego ahorcado
    '''
    #cargamos las plantillas
    plantillas = fn.carga_plantillas(nombre_plantilla)
    oraciones = fn.carga_archivo_text(archivo_texto)
    palabras = fn.obten_palabras(oraciones)
    o = 5 #oportunidades
    p = choice(palabras)
    abcdario = {letra:letra for letra in string.ascii_lowercase}
    adivinadas = set()
    while o > 0:
        fn.despliega_plantilla(plantillas,o)
        fn.adivina_letra(abcdario, p, adivinadas, o)
        o= fn.adivina_letra(abcdario,p, adivinadas,o)
        if p == ''.join([letra if letra in adivinadas else '_' for letra in p]):
            print('Ganaste')
            break
        #o -= 1
    fn.despliega_plantilla(plantillas,o)
    print(f"La palabra era: {p}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Juego del ahorcado')
    parser.add_argument('-a', '--archivo', help='Archivo de texto con palabras', default='./datos/pg15532.txt')
    args = parser.parse_args()
    archivo = args.archivo
    if os.stat(archivo) == False:
        print(f'El archivo "{archivo}"no existe')
        exit()
    #archivo = './datos/pg15532.txt'
    main(archivo)

