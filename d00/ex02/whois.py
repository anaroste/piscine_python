import sys


def main(argv):
    if len(argv) > 1:
        print('ERROR')
        return
    if argv[0][0] == '-':
        if not argv[0][1:].isnumeric():
            print('ERROR')
            return
    nb = int(argv[0])
    if nb == 0:
        print("I'm Zero.")
    elif nb % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


if __name__ == '__main__':
    main(sys.argv[1:])
