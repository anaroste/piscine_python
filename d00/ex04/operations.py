import sys


def usage(error=0):
    if error == 1:
        print('InputError: too many arguments\n')
    elif error == 2:
        print('InputError: only numbers\n')
    print('''Usage: python operations.py <number1> <number2>\nExample:\n
    python operations.py 10 3''')


def main(argv):
    if len(argv) == 0:
        return usage()
    elif len(argv) > 2:
        return usage(1)
    if not argv[0].isnumeric or not argv[1].isnumeric:
        return usage(2)

    a = int(argv[0])
    b = int(argv[1])
    div0 = 'ERROR (div by zero)'
    mod0 = 'ERROR (modulo by zero)'
    print(f"{'Sum:'.ljust(12)}{a + b}\n"
          f"{'Difference:'.ljust(12)}{a - b}\n"
          f"{'Product:'.ljust(12)}{a * b}\n"
          f"{'Quotient:'.ljust(12)}{a / b if b != 0 else div0}\n"
          f"{'Remainder:'.ljust(12)}{a % b if b != 0 else mod0}")


if __name__ == '__main__':
    main(sys.argv[1:])
