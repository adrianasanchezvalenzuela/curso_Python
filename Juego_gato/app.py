'''
Este archivo es el punto de entrada de la aplicación
'''
import tablero

def main():
    '''
    Función principal
    '''
    X = {"G": 0, "P":0, "E": 0}
    O = {"G": 0, "P":0, "E": 0}
    score = {"X":X,"O":O}
    numeros= [str(x) for x in range(1,10)]
    corriendo = True
    while corriendo:
        dsimbolos= {x:x for x in numeros}
        g = tablero.juego(dsimbolos)
        tablero.actualiza_score(score,g)
        tablero.despliega_tablero(score)
        seguir = input('Quieres seguir jugando? (s/n): ')
        if seguir.lower() == 'n':
            corriendo = False
    '''
    numeros= [str(x) for x in range(1,10)]
    dsimbolos= {x:x for x in numeros}
    g = tablero.juego(dsimbolos)
    if g is not None:
        print(f'El ganador es {g}')
    else:
        print('Empate')
    '''

if __name__ == '__main__':
    main()
