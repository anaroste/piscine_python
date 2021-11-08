def main():
    phrase = "The right format"
    aligned = '-' * 42

    print(f'{aligned[:42 - len(phrase)]}{phrase}')


if __name__ == '__main__':
    main()
