def what_are_the_vars(*args, **kwargs):
    obj = ObjectC()
    if len(args) == 0:
        return obj
    for key, value in kwargs.items():
        try:
            getattr(obj, key)
            return None
        except AttributeError:
            pass
        setattr(obj, key, value)
    for i in range(len(args)):
        try:
            getattr(obj, 'var_' + str(i))
            return None
        except AttributeError:
            pass
        setattr(obj, 'var_' + str(i), args[i])
    return obj


class ObjectC(object):
    def __init__(self):
        pass


def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != "_":
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")


if __name__ == "__main__":
    obj = what_are_the_vars(None)
    doom_printer(obj)
    print('-------------')
    obj = what_are_the_vars(lambda x: x, function=what_are_the_vars)
    doom_printer(obj)
    print('-------------')
    obj = what_are_the_vars(3, var_0=2)
    doom_printer(obj)
    print('-------------')

    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
