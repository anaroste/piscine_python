from PIL.Image import new
import numpy as np


class ColorFilter:
    def __init__(self):
        pass

    @staticmethod
    def invert(array):
        """
        Inverts the color of the image received as a numpy array.
        Args:
        array: numpy.ndarray corresponding to the image.
        Return:
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        This function should not raise any Exception.
        """
        for elt in array:
            for rgb in elt:
                rgb[0] = 1 - rgb[0]
                rgb[1] = 1 - rgb[1]
                rgb[2] = 1 - rgb[2]
        return array
        return array

    @staticmethod
    def to_blue(array):
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
        array: numpy.ndarray corresponding to the image.
        Return:
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        This function should not raise any Exception.
        """
        for elt in array:
            for rgb in elt:
                rgb[0], rgb[1] = 0, 0
        return array

    @staticmethod
    def to_green(array):
        """
        Applies a green filter to the image received as a numpy array.
        Args:
        array: numpy.ndarray corresponding to the image.
        Return:
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        This function should not raise any Exception.
        """
        for elt in array:
            for rgb in elt:
                rgb[0], rgb[2] = 0, 0
        return array

    @staticmethod
    def to_red(array):
        """
        Applies a red filter to the image received as a numpy array.
        Args:
        array: numpy.ndarray corresponding to the image.
        Return:
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        This function should not raise any Exception.
        """
        for elt in array:
            for rgb in elt:
                rgb[1], rgb[2] = 0, 0
        return array

    @staticmethod
    def to_celluloid(array):
        """
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        Remarks:
        celluloid filter is also known as cel-shading or toon-shading.
        Args:
        array: numpy.ndarray corresponding to the image.
        Return:
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        This function should not raise any Exception.
        """
        ret = np.array(array)
        echantillon = np.linspace(0.0, 1.0, num=4, endpoint=False)[::-1]
        for nb in echantillon:
            i_bool = array >= nb
            array[i_bool] = -1
            ret[i_bool] = nb
        return ret

    @staticmethod
    def to_grayscale(array, filter, **kwargs):
        """
        Applies a grayscale filter to the image received as a numpy array.
        For filter = ’mean’/’m’: performs the mean of RBG channels.
        For filter = ’weight’/’w’: performs a weighted mean of RBG channels.
        Args:
        array: numpy.ndarray corresponding to the image.
        filter: string with accepted values in [’m’,’mean’,’w’,’weight’]
        weights: [kwargs] list of 3 floats where the sum equals to 1,
        corresponding to the weights of each RBG channels.
        Return:
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        This function should not raise any Exception.
        """
        if filter in ['m', 'mean']:
            for elt in array:
                for rgb in elt:
                    rgb[0] = sum([rgb[0], rgb[1], rgb[2]]) / 3
                    rgb[1] = sum([rgb[0], rgb[1], rgb[2]]) / 3
                    rgb[2] = sum([rgb[0], rgb[1], rgb[2]]) / 3
        elif filter in ['w', 'weight']:
            for elt in array:
                for rgb in elt:
                    rgb[0] = sum([sum([rgb[0], kwargs['r'][0]]),
                                  sum([rgb[1], kwargs['r'][1]]),
                                  sum([rgb[2], kwargs['r'][2]])]) / 3
                    rgb[1] = sum([sum([rgb[0], kwargs['r'][0]]),
                                  sum([rgb[1], kwargs['r'][1]]),
                                  sum([rgb[2], kwargs['r'][2]])]) / 3
                    rgb[2] = sum([sum([rgb[0], kwargs['r'][0]]),
                                  sum([rgb[1], kwargs['r'][1]]), 
                                  sum([rgb[2], kwargs['r'][2]])]) / 3
        else:
            return None
        return array




from ImageProcessor import ImageProcessor
imp = ImageProcessor()
arr = imp.load("elon_canaGAN.png")
cf = ColorFilter()
# print(arr)
# arr2 = cf.to_celluloid(arr)
# arr2 = cf.to_grayscale(arr, 'm')
arr2 = cf.to_grayscale(arr, 'weight', r=[0.2, 0.3, 0.5])
# print(arr)
# print('--------------------')
# print(arr2)
# imp.display(arr)
imp.display(arr2)
