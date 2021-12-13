from random import randint


def generator(text, sep=" ", option=None):
    '''Option is an optional arg, sep is mandatory'''
    opt = [None, 'shuffle', 'ordered', 'unique']
    if option != None and not isinstance(option, str):
        print('ERROR')
        exit()
    if not isinstance(text, str) or opt.count(option) == 0:
        print('ERROR')
        exit()
    tab = text.split(sep)
    if option is None:
        for elt in tab:
            yield elt
    elif option == 'shuffle':
        while len(tab) != 0:
            i = randint(0, len(tab) - 1)
            yield tab[i]
            tab.pop(i)
    elif option == 'ordered':
        tab.sort()
        for elt in tab:
            yield elt
    elif option == 'unique':
        uniq = []
        for elt in tab:
            if uniq.count(elt) == 0:
                yield elt
                uniq.append(elt)
