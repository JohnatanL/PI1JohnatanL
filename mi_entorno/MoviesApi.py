import pandas as pd
import uvicorn
from fastapi import FastAPI

app = FastAPI()

df_movies = pd.read_csv('movies_dataset.csv')
df_credits = pd.read_csv('credits.csv')

@app.get('/cantidad_filmaciones_mes/{mes}')
def cantidad_filmaciones_mes(mes: str):
    cantidad = df_movies[df_movies['release_date'].str.contains(mes, case=False)].shape[0]
    return f"{cantidad} cantidad de películas fueron estrenadas en el mes de {mes}"

@app.get('/cantidad_filmaciones_dia/{dia}')
def cantidad_filmaciones_dia(dia: str):
    cantidad = df_movies[df_movies['release_date'].str.contains(dia, case=False)].shape[0]
    return f"{cantidad} cantidad de películas fueron estrenadas en los días {dia}"

@app.get('/score_titulo/{titulo_de_la_filmacion}')
def score_titulo(titulo_de_la_filmacion: str):
    peliculas = df_movies[df_movies['title'] == titulo_de_la_filmacion]
    if peliculas.empty:
        return f"No se encontró la película con el título {titulo_de_la_filmacion}"
    pelicula = peliculas.iloc[0]
    titulo = pelicula['title']
    anio_estreno = pelicula['release_date'].split('-')[0]
    score = pelicula['vote_average']
    return f"La película {titulo} fue estrenada en el año {anio_estreno} con un score/popularidad de {score}"

@app.get('/votos_titulo/{titulo_de_la_filmacion}')
def votos_titulo(titulo_de_la_filmacion: str):
    peliculas = df_movies[df_movies['title'] == titulo_de_la_filmacion]
    if peliculas.empty:
        return f"No se encontró la película con el título {titulo_de_la_filmacion}"
    pelicula = peliculas.iloc[0]
    titulo = pelicula['title']
    cantidad_votos = pelicula['vote_count']
    promedio_votos = pelicula['vote_average']
    if cantidad_votos < 2000:
        return f"La película {titulo} no cumple con la condición de tener al menos 2000 valoraciones."
    else:
        anio_estreno = pelicula['release_date'].split('-')[0]
        return f"La película {titulo} fue estrenada en el año {anio_estreno}. La misma cuenta con un total de {cantidad_votos} valoraciones, con un promedio de {promedio_votos}"

@app.get('/get_actor/{nombre_actor}')
def get_actor(nombre_actor: str):
    actor_movies = df_credits[df_credits['cast'].str.contains(nombre_actor, case=False)]
    cantidad_filmaciones = actor_movies.shape[0]
    promedio_retorno = actor_movies['id'].mean()
    return f"El actor {nombre_actor} ha participado en {cantidad_filmaciones} filmaciones, ha conseguido un retorno de {promedio_retorno} con un promedio de retorno por filmación de {promedio_retorno}"

@app.get('/get_director/{nombre_director}')
def get_director(nombre_director: str):
    director_movies = df_credits[df_credits['crew'].str.contains(nombre_director, case=False)]
    cantidad_filmaciones = director_movies.shape[0]
    promedio_retorno = director_movies['id'].mean()
    return f"El director {nombre_director} ha participado en {cantidad_filmaciones} filmaciones, ha conseguido un retorno de {promedio_retorno} con un promedio de retorno por filmación de {promedio_retorno}"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)