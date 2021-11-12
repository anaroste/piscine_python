import pandas as pd
from FileLoader import FileLoader


def HowManyMedals(df, name):
    df_name = df[df['Name'] == name]
    dico = {}
    for index, row in df_name.iterrows():
        if isinstance(row['Medal'], str):
            if list(dico.keys()).count(row['Year']) == 0:
                dico[row['Year']] = {'G': 0, 'S': 0, 'B': 0}
            dico[row['Year']][row['Medal'][0]] += 1
    return dico


loader = FileLoader()
data = loader.load("athlete_events.csv")
print(HowManyMedals(data, 'Kjetil Andr Aamodt'))
