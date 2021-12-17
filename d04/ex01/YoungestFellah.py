import pandas as pd
from FileLoader import FileLoader


def youngestfellah(df, year):
    """
    Get the name of the youngest woman and man for the given year.
    Args:
    df: pandas.DataFrame object containing the dataset.
    year: integer corresponding to a year.
    Returns:
    dct: dictionary with 2 keys for female and male athlete.
    """
    df_year = df[df['Year'] == year]
    df_f = df_year[df_year['Sex'] == 'F']
    df_m = df_year[df_year['Sex'] == 'M']
    f = df_f['Age'].min()
    m = df_m['Age'].min()
    return {'f': f, 'm': m}
