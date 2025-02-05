'''
Este archivo es el punto de entrada de la aplicación
'''
import tablero

def main():
    '''
    Función principal
    '''
    numeros= [str(x) for x in range(1,10)]
    dsimbolos= {x:x for x in numeros}
    g = tablero.juego(dsimbolos)
    if g is not None:
        print(f'El ganador es {g}')
    else:
        print('Empate')

if __name__ == '__main__':
    main()
