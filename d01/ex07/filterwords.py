import sys
import string


def main(argv):
    if len(argv) != 2 or not type(argv[0]) == str or not argv[1].isdigit():
        print('ERROR')
        return
    punct = string.punctuation.replace(' ', '')
    argv[0] = argv[0].translate(str.maketrans('', '', punct))
    tab = argv[0].split(' ')
    ret = []
    for elt in tab:
        if len(elt) > int(argv[1]):
            ret.append(elt)
    print(ret)


if __name__ == '__main__':
    main(sys.argv[1:])
