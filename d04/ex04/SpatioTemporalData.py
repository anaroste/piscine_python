import pandas as pd
from FileLoader import FileLoader


class SpatioTemporalData:
    def __init__(self, df):
        self.df = df

    def when(self, location):
        df_lieu = self.df[self.df['City'] == location]
        ret = []
        for i, row in df_lieu.iterrows():
            if ret.count(row['Year']) == 0:
                ret.append(row['Year'])
        return ret

    def where(self, date):
        df_lieu = self.df[self.df['Year'] == date]
        ret = []
        for i, row in df_lieu.iterrows():
            if ret.count(row['City']) == 0:
                ret.append(row['City'])
        return ret


loader = FileLoader()
data = loader.load("athlete_events.csv")
st = SpatioTemporalData(data)
print(st.where(2016))
print(st.when('Athina'))
