from fastapi import FastAPI
import pandas as pd
from sklearn.metrics.pairwise import cosine similarity

app = FastAPI()

@app.get('/')
def index():
    return {'Primer PI para Henry Data Science'}

@app.get('/PlayTimeGenre/{genero}')
def PlayTimeGenre(genero: str):

    df_ep01 = pd.read_csv('endpoint01.csv')

    # Filtrar el DataFrame para el género específico
    filtered_df = df_ep01[df_ep01['genero'] == genero]
          
    # Construye el response
    response = {"Año de lanzamiento con más horas jugadas para {}: {}".format(genero,filtered_df['release_year'] )}

    # Muestra el resultado
    return response