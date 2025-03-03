from athlete import Athlete
from Sport import Sport
from Team import Team
from Game import Game
import json
import game_logic as gl
import sys
import os


def main(archivo_torneo:str):
    """
    Funcion principal ed games
    """
    if archivo_torneo != "":
        with (open(archivo_torneo,"r", encoding="utf-8")) as f:
            torneo = json.load(f)
    else:
        gl.create_gamefile()
        archivo_torneo = "torneo.json"
        with (open(archivo_torneo,"r", encoding="utf-8")) as f:
            torneo = json.load(f)
    # Jugar todos los juegos del torneo
    gl.play_game(torneo)
    #Calculamos el tablero de puntuación
    #for juego in torneo:
        #print(juego['score'])
    #torneo = gl.json_to_tournament(torneo)
    tablero = gl.scoring(torneo)
    gl.display_tablero(tablero)

if __name__ == "__main__":
    archivo_torneo = "torneo.json"
    main(archivo_torneo)