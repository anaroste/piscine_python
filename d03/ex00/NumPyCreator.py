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
        if not check_all_elt_type(tpl, tuple) or not check_all_elt_len(tpl):
            return None
        return np.array(tpl)

    def from_iterable(self, itr):
        return [x for x in itr]

    def from_shape(self, shape, value=0):
        row = [value for i in range(shape[1])]
        return [row for i in range(shape[0])]

    def random(self, shape):
        row = [random.random() for i in range(shape[1])]
        return [row for i in range(shape[0])]

    def identity(self, n):
        ret = []
        for i in range(n):
            tmp = []
            for j in range(n):
                if i == j:
                    tmp.append(1)
                else:
                    tmp.append(0)
            ret.append(tmp)
        return ret


npc = NumPyCreator()
# lst = [[1, 2, 3], [4, 5, 6]]
# tpl = ((1,2,3), (4,5,6))
# print(type(npc.from_list(lst)))
# print(npc.from_list(lst))
# print(npc.from_list(((1,2),(3,4))))
# print(npc.from_tuple([[1,2,3],[6,3,4]]))
# print(npc.from_iterable(range(5)))
# print(npc.from_list([[1,2,3],['a','b','c'],[6,4,7]]))
# print(type(npc.from_list([[1,2,3],['a','b','c'],[6,4,7]])))
# print(type(npc.from_tuple(tpl)))
# itr = "Hello my old friend"
# print(npc.from_iterable(itr))
# print(npc.from_shape((3,5)))
# print(npc.random((4,5)))
# print(npc.identity(5))