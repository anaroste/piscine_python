import numpy as np


def check_all_elt_type(itr, type):
    for elt in itr:
        if not isinstance(elt, type):
            return False
    return True


def check_all_elt_len(itr):
    if len(itr) == 0:
        return True
    len_elt = len(itr[0])
    for elt in itr:
        if len(elt) != len_elt:
            return False
    return True


def isshape(shape):
    if not isinstance(shape, tuple) and len(shape) != 2:
        return False
    if not isinstance(shape[0], int) and not isinstance(shape[1], int):
        return False
    return True


def isaxis(axis):
    if axis != 0 and axis != 1:
        return False
    return True


class ScrapBooker:
    def __init__(self):
        pass

    def crop(self, array, dim, position=(0, 0)):
        '''
        Crops the image as a rectangle via dim arguments (being the new height
        and width oof the image) from the coordinates given by position
        arguments.
        Args:
        array: numpy.ndarray
        dim: tuple of 2 integers.
        position: tuple of 2 integers.
        Returns:
        new_arr: the cropped numpy.ndarray.
        None otherwise (combinaison of parameters not incompatible).
        Raises:
        This function should not raise any Exception.
        '''
        if not isinstance(array, np.ndarray):
            return None
        if not check_all_elt_len(array):
            return None
        if not isshape(dim) and not isshape(position):
            return None
        return array[position[0]:position[0] + dim[0],
                     position[1]:position[1] + dim[1]]

    def thin(self, array, n, axis):
        '''
        Deletes every n-th line pixels along the specified axis
        (0: vertical, 1: horizontal)
        Args:
        array: numpy.ndarray.
        n: non null positive integer lower than the number of row/column of
        the array (depending of axis value).
        axis: positive non null integer.
        Returns:
        new_arr: thined numpy.ndarray.
        None otherwise (combinaison of parameters not incompatible).
        Raises:
        This function should not raise any Exception.
        '''
        if not isaxis(axis) or len(array) < n:
            return None
        ret = []
        if axis == 1:
            for i in range(len(array)):
                if (i + 1) % n != 0:
                    ret.append(array[i])
        else:
            for elt in array:
                tmp = []
                for i in range(len(elt)):
                    if (i + 1) % n != 0:
                        tmp.append(elt[i])
                ret.append(tmp)
        return np.array(ret)

    def juxtapose(self, array, n, axis):
        '''
        Juxtaposes n copies of the image along the specified axis.
        Args:
        array: numpy.ndarray.
        n: positive non null integer.
        axis: integer of value 0 or 1.
        Returns:
        new_arr: juxtaposed numpy.ndarray.
        None otherwise (combinaison of parameters not incompatible).
        Raises:
        This function should not raise any Exception.
        '''
        if not isaxis(axis) or len(array) < n or n < 0:
            return None
        ret = array
        for i in range(n - 1):
            ret = np.concatenate((ret, array), axis)
        return np.array(ret)

    def mosaic(self, array, dim):
        '''
        Makes a grid with multiple copies of the array. The dim argument
        specifies the number of repetition along each dimensions.
        Args:
        array: numpy.ndarray.
        dim: tuple of 2 integers.
        Returns:
        new_arr: mosaic numpy.ndarray.
        None otherwise (combinaison of parameters not incompatible).
        Raises:
        This function should not raise any Exception.
        '''
        if not isshape(dim) or len(dim) != 2:
            return None

        return np.tile(array, dim)

# spb = ScrapBooker()
# arr1 = np.arange(0,25).reshape(5,5)
# print(spb.crop(arr1, (3,1),(1,0)))
# arr2 = np.array("A B C D E F G H I J Q L".split() * 6).reshape(-1,12)
# print(arr2)
# print('--------------')
# print(spb.thin(arr2,3,1))
# arr3 = np.array([['A', 'B'],['C', 'D']])
# print(spb.juxtapose(arr3, 3, 1))
# print(spb.mosaic(arr3, (3,2)))
