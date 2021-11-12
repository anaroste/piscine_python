import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import os.path


class ImageProcessor:
    def __init__(self):
        pass

    def load(self, path):
        ret = None
        try:
            ret = mpimg.imread(path)
            sha = ret.shape
            print(f"Loading image of dimensions {sha[0]} x {sha[1]}")
        except FileNotFoundError:
            print('Exception: FileNotFoundError -- strerror:',
                  'No such file or directory')
        except SyntaxError:
            print('Exception: OSError -- strerror: None')
        return ret

    def display(self, array):
        try:
            imgplot = plt.imshow(array)
            plt.show()
        except TypeError:
            return
