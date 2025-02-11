'''
funciones auxiliares
'''

def carga_archivo_text(archivo:str)->list:
    '''
    Carga un archivo de texto y devuelve una lista con las oraciones del archivo
    '''
    with open(archivo, 'r', encoding='utf-8') as file:
        oraciones = file.readlines()
    return oraciones

def carga_plantillas(nombre_plantillas:str)->dict:
    '''
    Carga las plantillas del juego a partir de un archivo de texto
    '''
    plantillas = {}
    for i in range(6):
        plantillas[i] = carga_archivo_text(f'./plantillas/{nombre_plantillas}-{i}.txt')
    return plantillas
    
def despliega_plantilla(diccionario:dict,nivel:int):
    '''
    Despliega la platilla del juego
    '''
    if nivel <= 5:
        plantilla = diccionario[nivel]
        for renglon in plantilla:
            print(renglon)

if __name__ == '__main__':
    plantilla = carga_plantillas('plantilla')
    despliega_plantilla(plantilla,5)
    lista_oraciones = carga_archivo_text('./datos/pg15532.txt')
    print(lista_oraciones[110:115])
    texto = "".join(lista_oraciones[110:])
    print(texto[:100])




'''
    lista = carga_archivo_text('./plantillas/plantilla-0.txt')
    for elemento in lista:
        print(elemento)
'''