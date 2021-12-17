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


# loader = FileLoader()
# data = loader.load("../ressources/athlete_events.csv")
# mpl = MyPlotLib()
# mpl.histogram(data, ['Age'])
# mpl.histogram(data, ['Weight', 'Height'])
# mpl.histogram(data, ['Weight', 'Height', 'Age'])
# mpl.density(data, ['Age'])
# mpl.density(data, ['Weight', 'Height'])
# mpl.density(data, ['Weight', 'Height', 'Age'])
# mpl.pair_plot(data, ['Age'])
# mpl.pair_plot(data, ['Weight', 'Height'])
# mpl.pair_plot(data, ['Weight', 'Height'])
# mpl.pair_plot(data, ['Weight', 'Height', 'Age'])
# mpl.box_plot(data, ['Age'])
# mpl.box_plot(data, ['Weight', 'Height'])
# mpl.box_plot(data, ['Weight', 'Height', 'Age'])
