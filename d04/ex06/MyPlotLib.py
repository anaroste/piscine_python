import pandas as pd
from pandas.core.frame import DataFrame
from FileLoader import FileLoader
import matplotlib.pyplot as plt
import seaborn as sns


class MyPlotLib:
    def __init__(self):
        pass

    def histogram(self, data, features):
        for column in data:
            if features.count(column) != 0:
                plt.hist(data[column])
                plt.title(column)
                plt.show()

    def density(self, data, features):
        for column in data:
            if features.count(column) != 0:
                sns.displot(data[column], kind="kde")
                plt.title(column)
                plt.show()

    def pair_plot(self, data, features):
        df = DataFrame(data, columns=features)
        sns.pairplot(df)
        plt.show()

    def box_plot(self, data, features):
        df = pd.DataFrame(data, columns=features)
        sns.boxplot(data=df)
        plt.show()


loader = FileLoader()
data = loader.load("athlete_events.csv")
mpl = MyPlotLib()
# mpl.histogram(data, ['Age', 'Year'])
mpl.box_plot(data, ['Weight', 'Height'])
