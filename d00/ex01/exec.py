import sys


def main(argv):
    to_print = ''
    for arg in argv:
        tmp = ''
        for elt in arg:
            if elt.isupper():
                tmp += elt.lower()
            else:
                tmp += elt.upper()
        to_print += ' ' + tmp
    print(to_print[::-1])


if __name__ == '__main__':
    main(sys.argv[1:])
