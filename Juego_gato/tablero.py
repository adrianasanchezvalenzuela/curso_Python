'''
tablero.py: Dibuja el tablero del juego del gato
'''
import random
def dibuja_tablero(simbolos:dict):
    '''
    Dibuja el tablero del juego del gato
    '''
    print(f'''
          {simbolos['1']} | {simbolos['2']} | {simbolos['3']}
          ----------
          {simbolos['4']} | {simbolos['5']} | {simbolos['6']}
          ----------
          {simbolos['7']} | {simbolos['8']} | {simbolos['9']}
          ''')

'''
Funcion para una lista de casillas libres para la ia
'''
def casillas_libres(simbolos: dict):
    '''
    Devuelve una lista con casillas que todavia estan disponibles
    '''
    return [key for key, value in simbolos.items() if value not in ['X','O']]

def ia(simbolos:dict, lista_combinaciones: list, simbolo_ia:str, simbolo_usuario: str):
    ''' Juega la maquina'''
    print("Turno de la maquina")
    casillas = casillas_libres(simbolos)

    '''
    La IA busca ganar en la siguiente jugada
    '''
    for c in casillas:
        simbolos_copia = simbolos.copy()
        simbolos_copia[c] = simbolo_ia
        if check_winner(simbolos_copia, lista_combinaciones) == simbolo_ia:
            simbolos[c] = simbolo_ia
            return
        
    '''
    La IA bloquea al jugador si va a ganar
    '''
    for c in casillas:
        simbolos_copia = simbolos.copy()
        simbolos_copia[c] = simbolo_usuario
        if check_winner(simbolos_copia, lista_combinaciones) == simbolo_usuario:
            simbolos[c] = simbolo_ia
            return
        
    '''
    La IA da preferencia al centro si esta disponible
    '''
    if '5' in casillas:
        simbolos['5'] = simbolo_ia
        return
    
    '''
    La IA da preferencia a las esquinas
    '''
    esquinas = ['1', '3', '7', '9']
    esquinas_libres = [c for c in casillas if c in esquinas]
    if esquinas_libres:
        simbolos[random.choice(esquinas_libres)] = simbolo_ia
        return
    
    '''
    La IA escoge al al azar si no hay jugada
    '''
    simbolos[random.choice(casillas)] = simbolo_ia


def usuario(simbolos:dict, simbolo_usuario: str):
    ''' Juega el usuario'''
    lista_numeros = [str(i) for i in range(1,10)] #del 1 al 9
    ocupado = True
    while ocupado is True:
        x = input('Ingresa el número de la casilla: ')
        if x in lista_numeros:
            if simbolos[x] not in ['X','O']:
                simbolos[x] = simbolo_usuario
                ocupado = False
            else:
                print('Casilla ocupada')
        else:
            print('Numero incorrecto')


def juego(simbolos:dict, simbolo_usuario: str, simbolo_ia: str):
    '''
    Juego del gato
    '''
    lista_combinaciones = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['1', '4', '7'],
    ['2', '5', '8'],
    ['3', '6', '9'],
    ['1', '5', '9'],
    ['3', '5', '7']
    ]
    
    en_juego = True
    movimientos = 0
    gana = None
    dibuja_tablero(simbolos)
    while en_juego:
        if movimientos % 2 == 0: #Si es par es el turno de usuario
            usuario(simbolos, simbolo_usuario)

        else: #Si es impar, es el turno de la IA
            ia(simbolos, lista_combinaciones, simbolo_ia, simbolo_usuario)


        movimientos += 1
        gana = check_winner(simbolos, lista_combinaciones)
        if gana is not None:
            en_juego = False
            continue
        if movimientos >= 9:
            en_juego=False
            continue
        
        ia(simbolos, lista_combinaciones,simbolo_ia, simbolo_usuario)
        dibuja_tablero(simbolos)
        movimientos += 1
        gana = check_winner(simbolos, lista_combinaciones)
        if gana is not None:
            en_juego = False
            continue
        if movimientos>=9:
            en_juego = False
            continue
        dibuja_tablero(simbolos)
        
    return gana

def check_winner(simbolos:dict,combinaciones:list):
    '''
    Checa si hay un ganador
    '''
    for c in combinaciones:
        if simbolos[c[0]] == simbolos[c[1]] == simbolos[c[2]]:
           return simbolos[c[0]]
    return None

def actualiza_score(score:dict,ganador:str):
    ''' Actualiza el score'''
    X = score["X"]
    O = score["O"]
    if ganador is not None:
        print(f'El ganador es {ganador}')
        if ganador == 'X':
            X["G"] += 1
            O["P"] += 1
        elif ganador == 'O':
            O["G"] += 1
            X["P"] += 1
        else:
            O["E"] += 1
            X["E"] += 1
    else:
        print("Empate")
        O["E"] += 1
        X["E"] += 1

if __name__ == '__main__':
    numeros= [str(x) for x in range(1,10)]
    dsimbolos= {x:x for x in numeros}
    g = juego(dsimbolos)
    if g is not None:
        print(f'El ganador es {g}')
    else:
        print('Empate')

def despliega_tablero(score:dict):
    '''Despliega el tablero de score'''
    print(f'''
    X | G: {score["X"] ["G"]} | P: {score["X"] ["P"]} | E: {score["X"] ["E"]}
    O | G: {score["O"] ["G"]} | P: {score["O"] ["P"]} | E: {score["O"] ["E"]}
    ''')

    '''
    dibuja_tablero(dsimbolos)
    ia(dsimbolos)
    dibuja_tablero(dsimbolos)
    usuario(dsimbolos)
    dibuja_tablero(dsimbolos)

    x = random.choice(numeros)
    numeros.remove(x)
    dsimbolos[x] = 'X'
    dibuja_tablero(dsimbolos)
    o =random.choice(numeros)
    numeros.remove(o)
    dsimbolos[o] = 'O'
    dibuja_tablero(dsimbolos)
    print(numeros)
    '''