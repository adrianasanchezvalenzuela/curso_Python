'''Programa principal de MoviesDB'''
 
from flask import Flask, request, url_for, redirect, render_template
import os
import random
import movie_classes as mc
 
app = Flask(__name__)
sistema = mc.SistemaCine()
archivo_actores = "datos/movies_db - actores.csv"
archivo_peliculas = "datos/movies_db - peliculas.csv"
archivo_relaciones = "datos/movies_db - relaciones.csv"
archivo_usuarios = "datos/movies_db - users_hashed.csv"
sistema.cargar_csv(archivo_actores, mc.Actor)
sistema.cargar_csv(archivo_peliculas, mc.Pelicula)
sistema.cargar_csv(archivo_relaciones, mc.Relaciones)
sistema.cargar_csv(archivo_usuarios, mc.User)
 
@app.route('/')
def index():
    '''Página principal de la aplicación'''
    return render_template('index.html')

@app.route('/actores')
def actores():
    '''Muestra lista de actores'''
    actores = sistema.actores.values()
    return render_template('actores.html', actores = actores)

@app.route('/peliculas')
def peliculas():
    '''Muestra lista de peliculas'''
    peliculas = sistema.peliculas.values()
    return render_template('peliculas.html', peliculas = peliculas)

@app.route('/actor/<int:id_actor>') 
def actor(id_actor):
    """Muestra información de un actor"""
    actor = sistema.actores.get(id_actor)  
    if actor:
        personajes = sistema.obtener_personajes_por_estrella(id_actor)
        return render_template('actor.html', actor=actor, lista_peliculas=personajes)
    else:
        return "Película no encontrada", 404


@app.route('/pelicula/<int:id_pelicula>')
def pelicula(id_pelicula):
    """Muestra información de una película"""
    pelicula = sistema.peliculas.get(id_pelicula)
    if pelicula:
        personajes = sistema.obtener_personajes_por_pelicula(id_pelicula)
        return render_template('pelicula.html', pelicula=pelicula, lista_actores=personajes)
    else:
        return "Película no encontrada", 404
 

if __name__ == '__main__':
    app.run(debug=True)