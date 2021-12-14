import numpy as np
import random


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


class NumPyCreator:
    def __init__(self):
        pass

    def from_list(self, lst):
        if not check_all_elt_type(lst, list) or not check_all_elt_len(lst):
            return None
        return np.array(lst)

    def from_tuple(self, tpl):
        if not isinstance(tpl, tuple) or not check_all_elt_len(tpl):
            return None
        return np.array(tpl)

    def from_iterable(self, itr):
        return np.array([x for x in itr])

    def from_shape(self, shape, value=0):
        if shape[0] < 0 or shape[1] < 0:
            return None
        row = [float(value) for i in range(shape[1])]
        return np.array([row for i in range(shape[0])])

    def random(self, shape):
        row = [random.random() for i in range(shape[1])]
        return np.array([row for i in range(shape[0])])

    def identity(self, n):
        if n < 0:
            return None
        ret = []
        for i in range(n):
            tmp = []
            for j in range(n):
                if i == j:
                    tmp.append(1)
                else:
                    tmp.append(0)
            ret.append(tmp)
        return np.array(ret)
