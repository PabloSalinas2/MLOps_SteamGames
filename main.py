from fastapi import FastAPI
import pandas as pd


df_funcion1=pd.read_csv('funcion1.csv')
df_funcion2=pd.read_csv('funcion2.csv')
df_funcion3=pd.read_csv('funcion3.csv')
df_funcion4=pd.read_csv('funcion4.csv')
df_funcion5=pd.read_csv('funcion5.csv')

app= FastAPI()

@app.get("/")
def PlayTimeGenre( genre : str ): #  Debe devolver año con mas horas jugadas para dicho género.
    # pasar a dataframe dentro de la funcion ?

    try:
        genre=genre.capitalize()
        valor_maximo=df_funcion1[df_funcion1['genero']==genre]['timpo_total_jugado'].max()
        indice=df_funcion1[df_funcion1['timpo_total_jugado']==valor_maximo].index
        resultado=df_funcion1['año_lanzamiento'].loc[indice].values
        return {f'Año de lanzamiento con mas horas jugadas para el Género {genre}:':resultado[0]}
    except Exception as e:
        print('Genero incorrecto')



def UserForGenre( genero : str ): 
    try:
        genero=genero.capitalize() 
        df_genero=df_funcion2[df_funcion2['genero']==genero]
        tiempo_maximo=df_genero['timpo_total_jugado'].max()
        indice_tiempo_maximo=df_genero[df_genero['timpo_total_jugado']==tiempo_maximo].index
        resultado=df_genero['user_id'].loc[indice_tiempo_maximo].values[0]

        df_horas_por_año=df_funcion2[(df_funcion2['user_id']==resultado) & (df_funcion2['genero']==genero)]
        lista=[]
        for indice,fila in df_horas_por_año.iterrows():
            año=fila['año_posted_review']
            horas_jugadas=fila['timpo_total_jugado']
            lista.append({'Año': año, 'Horas': horas_jugadas})

        return {f'Usuario con más horas jugadas para el Género {genero}':resultado, 'Horas jugadas': lista}

    except Exception as e:
        return {'Genero incorrecto'}





def UsersRecommend( año : int ):
    try:
        df_top3=df_funcion3[df_funcion3['año_posted_review']==año].nlargest(3,'recommend')
        return [{'Puesto 1': df_top3['title'].iloc[0]},{'Puesto 2:': df_top3['title'].iloc[1]},{'Puesto 3:': df_top3['title'].iloc[2]}]

    except Exception:
        return {'No existen datos para el valor ingresado'}
    




def UsersNotRecommend( año : int ): # Devuelve el top 3 de juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)
    try:
        df_top3=df_funcion3[df_funcion3['año_posted_review']==año].nsmallest(3,'recommend')
        return [{'Puesto 1': df_top3['title'].iloc[0]},{'Puesto 2:': df_top3['title'].iloc[1]},{'Puesto 3:': df_top3['title'].iloc[2]}]

    except Exception:
        return {'No existen datos para el valor ingresado'}






def sentiment_analysis( año : int ): 
    df_año=df_funcion5[df_funcion5['año_lanzamiento']==año]
    positivos=0
    negativos=0
    neutros=0
    for i in df_año['sentiment_analysis'].values:
        if i==0:
            negativos+=1
        elif i==1:
            neutros+=1
        elif i==2:
            positivos+=1

    return {'Negative': negativos, 'Neutral': neutros,'Positive':positivos}


