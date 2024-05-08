from fastapi import FastAPI
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

@app.get('/')
def index():
    return {'Proyecto Individual 01'}

@app.get('/PlayTimeGenre/{genero}')
def PlayTimeGenre(genero: str):

    df_ep01 = pd.read_csv('endpoint01.csv')

    # Filtrar el DataFrame para el género específico
    filtered_df = df_ep01[df_ep01['genero'] == genero]
          
    # Construye el response
    response = {"Año de lanzamiento con más horas jugadas para {}: {}".format(genero,filtered_df.iloc[0]['release_year'] )}

    # Muestra el resultado
    return response

@app.get('/UserForGenre/{genero}')
def UserForGenre( genero : str ):
    df_ep02 = pd.read_csv('endpoint02.csv')

    filtered_df = df_ep02[df_ep02['genero'] == genero]
    response = {"Usuario con más horas jugadas para {}: {},'Horas jugadas' {}".format(filtered_df.iloc[0]['genero'],filtered_df.iloc[0]['usuario'],filtered_df.iloc[0]['anios_Horas'] )}
    return response