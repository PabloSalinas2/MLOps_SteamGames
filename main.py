from fastapi import FastAPI
import pandas as pd


df_funcion1=pd.read_csv('funcion1.csv')

app= FastAPI()

@app.get("/")
def PlayTimeGenre( genre : str ): #  Debe devolver año con mas horas jugadas para dicho género.
    # pasar a dataframe dentro de la funcion ?

    try:
        valor_maximo=df_funcion1[df_funcion1['genero']==genre]['timpo_total_jugado'].max()
        indice=df_funcion1[df_funcion1['timpo_total_jugado']==valor_maximo].index
        resultado=df_funcion1['año_lanzamiento'].loc[indice].values
        return {f'Año de lanzamiento con mas horas jugadas para el Género {genre}:':resultado[0]}
    except Exception as e:
        print('Genero incorrecto')



