def exposant(nb):
    ret = '-' if nb < 0 else ''
    nb_c = str(nb).split('.')[0]
    if nb_c[0] == '-':
        nb_c = nb_c[1:]
    try:
        c1 = nb_c[1]
    except IndexError:
        c1 = 0
    try:
        c2 = nb_c[2]
    except IndexError:
        c2 = 0
    ret += f"{nb_c[0]}.{c1}{c2}e+{len(nb_c) - 1}"
    return (ret)


def main():
    t = (0, 4, 132.42222, 10000, 12345.67)
    nb = round(t[2], 2)
    print('module_{:02d}, ex{:02d} : {},'.format(t[0], t[1], nb), end='')
    print(f'{exposant(t[3])}, {exposant(t[4])}')


if __name__ == '__main__':
    main()
