import pandas as pd
from pandas.core.frame import DataFrame

class FileLoader:
    def __init__(self):
        pass

    def load(self, path):
        ret = None
        try:
            ret = pd.read_csv(path)
            sha = ret.shape
            print(f"Loading dataset of dimensions {sha[0]} x {sha[1]}")
        except FileNotFoundError:
            print('Exception: FileNotFoundError -- strerror:',
                  'No such file or directory')
        except SyntaxError:
            print('Exception: OSError -- strerror: None')
        return ret

    def display(self, data, nb):
        if not isinstance(nb, int) or not isinstance(data, DataFrame):
            return
        if nb < 0: 
            nb *= -1
            print(data.tail(nb))
        else:
            print(data.head(nb))
        
# loader = FileLoader()
# data = loader.load("athlete_events.csv")
# loader.display(data, -5)