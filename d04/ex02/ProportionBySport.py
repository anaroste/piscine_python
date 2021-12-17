import pandas as pd
from FileLoader import FileLoader
import math


def truncate(number, decimals=0):
    """
    Returns a value truncated to a specific number of decimal places.
    """
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer.")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more.")
    elif decimals == 0:
        return math.trunc(number)

    factor = 10.0 ** decimals
    return math.trunc(number * factor) / factor


def proportionBySport(df, year, sport, sex):
    df_year = df[df['Year'] == year]
    df_sex = df_year[df_year['Sex'] == sex]
    df_sport = df_sex[df_sex['Sport'] == sport]
    return truncate(df_sport.shape[0] / df_sex.shape[0], 5)
