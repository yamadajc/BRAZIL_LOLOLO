import pandas as pd 
import os 


def fusion_concatenado(lista_ar):
    df_final = pd.DataFrame()
    for i in lista_ar:
        df_cosas = pd.read_csv(f"../datos/{i}",sep=";", encoding= "latin_1")
        nombre = i.replace(".","-").split("-")[1]+"_df"
        nombre = df_cosas.copy()
        df_final = pd.concat([df_final, nombre], axis = 0)

    return df_final