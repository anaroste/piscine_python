import pandas as pd
from FileLoader import FileLoader


def proportionBySport(df, year, sport, sex):
    df_year = df[df['Year'] == year]
    df_sex = df_year[df_year['Sex'] == sex]
    df_sport = df_sex[df_sex['Sport'] == sport]
    return df_sport.shape[0] / df_sex.shape[0]


loader = FileLoader()
data = loader.load("athlete_events.csv")
print(proportionBySport(data, 2004, 'Tennis', 'F'))