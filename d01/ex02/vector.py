def check_liste(liste):
    for elt in liste:
        if not isinstance(elt, float):
            return False
    return True


def define_arg(arg):
    tab = []
    if isinstance(arg, list):
        if isinstance(arg[0], list):
            for elt in arg:
                if not check_liste(elt):
                    print("Liste incorrect")
                    exit()
            tab = arg
        elif isinstance(arg[0], float) and check_liste(arg):
            tab = arg
        else:
            print("Liste incorrect")
            exit()
    elif isinstance(arg, tuple):
        if len(arg) != 2 or not isinstance(arg[0], int) \
           or not isinstance(arg[1], int):
            print("Tuple incorrect")
            exit()
        for i in range(arg[0], arg[1]):
            tab.append([float(i)])
    elif isinstance(arg, int):
        for i in range(arg):
            tab.append([float(i)])
    else:
        print("Type de l'argument non gere")
        exit()
    if isinstance(tab[0], list):
        dim = (len(tab), len(tab[0]))
    else:
        dim = (1, len(tab))
    return tab, dim


def init_tab(shape):
    r = []
    for i in range(shape[1]):
        r.append(0)
    tab = []
    for i in range(shape[0]):
        tab.append(r.copy())
    return tab


class Vector:
    def __init__(self, arg):
        tab, dim = define_arg(arg)

        self.values = tab
        self.shape = dim

    def dot(self, other):
        if other.shape == self.shape:
            tab = init_tab(self.shape)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    tab[i][j] = self.values[i][j] * other.values[i][j]
            return tab
        else:
            print("Les matrices n'ont pas la meme dimension")
            return None

    def T(self):
        tab = init_tab((self.shape[1], self.shape[0]))
        for i in range(len(self.values)):
            for j in range(len(self.values[i])):
                tab[j][i] = self.values[i][j]
        self.values = tab

    def __add__(self, other):
        if other.shape == self.shape:
            tab = init_tab(self.shape)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    tab[i][j] = self.values[i][j] + other.values[i][j]
            return tab
        else:
            print("Les matrices n'ont pas la meme dimension")
            return None

    __radd__ = __add__

    def __sub__(self, other):
        if other.shape == self.shape:
            tab = init_tab(self.shape)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    tab[i][j] = self.values[i][j] - other.values[i][j]
            return tab
        else:
            print("Les matrices n'ont pas la meme dimension")
            return None

    __rsub__ = __sub__

    def __truediv__(self, oth):
        if ((isinstance(oth, int) or isinstance(oth, float)) and oth != 0):
            tab = init_tab(self.shape)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    tab[i][j] = self.values[i][j] / oth
            return tab
        else:
            if oth == 0:
                raise ValueError("A scalar cannot be divided by a Vector")
            else:
                print("Erreur, division par autre chose qu'un int ou un float")
            return None

    def __rtruediv__(self, other):
        print("Erreur, impossible div scalaraire par vecteur")
        return None

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            tab = init_tab(self.shape)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    tab[i][j] = self.values[i][j] * other
            return tab
        else:
            print("Erreur, mul par autre chose qu'un int ou un float")
            return None

    def __rmul__(self, other):
        print("Erreur, impossible mul scalaraire par vecteur")
        return None

    def __str__(self):
        return f"Dimension : {self.shape}\n{self.values}"

    def __repr__(self):
        return f"{self.shape}-{self.values}"
