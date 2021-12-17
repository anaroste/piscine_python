import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class Komparator:
    def __init__(self, df):
        self.df = df

    def compare_histograms(self, categorical_var, numerical_var):
        nb = len(self.df[categorical_var].drop_duplicates())

        f, ax = plt.subplots(1, nb - 1, figsize=(9, 4))
        for i, elem in enumerate(self.df[categorical_var].drop_duplicates()):
            ax[i - 1].set_title(elem)
            sns.distplot(self.df[numerical_var][self.df[categorical_var] == elem].dropna(),
                         kde=False, rug=False, ax=ax[i - 1], hist=True,
                         hist_kws={"alpha": 1, "color": "dodgerblue"})
        plt.show()

    def density(self, categorical_var, numerical_var):
        plt.figure(figsize=(6, 4))
        for i, elem in enumerate(self.df[categorical_var].drop_duplicates()):
            sns.kdeplot(self.df[numerical_var][self.df[categorical_var] == elem].dropna(), label=elem)
        plt.title(categorical_var)
        plt.show()

    def compare_box_plots(self, categorical_var, numerical_var):
        nb = len(self.df[categorical_var].drop_duplicates())
        f, ax = plt.subplots(1, nb - 1, figsize=(9, 4))
        for i, elem in enumerate(self.df[categorical_var].drop_duplicates()):
            ax[i - 1].set_title(elem)
            sns.boxplot(x=self.df[numerical_var][self.df[categorical_var] == elem].dropna(),
                        ax=ax[i - 1], color='dodgerblue')
        plt.show()


from FileLoader import FileLoader
loader = FileLoader()
data = loader.load('../ressources/athlete_events.csv')
kp = Komparator(data)
kp.compare_box_plots("Medal", "Age")
kp.compare_histograms("Medal", "Height")
kp.density("Medal", "Weight")