'''
Este archivo es el punto de entrada de la aplicación
'''
import tablero
import argparse
import random


def main(usuario, simbolo_usuario):
    print(f"Hola {usuario}")
    print(f"Eres {simbolo_usuario}")
    '''
    Función principal
    '''
    X = {"G": 0, "P":0, "E": 0}
    O = {"G": 0, "P":0, "E": 0}
    score = {"X":X,"O":O}
    numeros= [str(x) for x in range(1,10)]
    corriendo = True

    # Asignar el turno inicial
    if simbolo_usuario == 'X':
        simbolo_ia = 'O'
    else:
        simbolo_ia = 'X'


    while corriendo:
        dsimbolos= {x:x for x in numeros}
        
        print(f"Empieza {usuario} con el simbolo {simbolo_usuario}")
        g = tablero.juego(dsimbolos, simbolo_usuario, simbolo_ia)


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
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', type=str, help='Nombre del Usuario', default='usuario')
    parser.add_argument('-s', type=str, choices = ['X', 'O'], help='Simbolo del Usuario', default='X')
    args = parser.parse_args()
    main(args.u, args.s)
