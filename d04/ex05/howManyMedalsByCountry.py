import pandas as pd
from FileLoader import FileLoader


def howManyMedalsByCountry(df, country):
    df_country = df[df['Team'] == country]
    dico = {}
    for index, row in df_country.iterrows():
        if isinstance(row['Medal'], str):
            if list(dico.keys()).count(row['Year']) == 0:
                dico[row['Year']] = {'G': 0, 'S': 0, 'B': 0}
            dico[row['Year']][row['Medal'][0]] += 1
    return dico
