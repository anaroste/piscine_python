def main():
    t = (3, 30, 2019, 9, 25)

    print(
        '{:02d}/{:02d}/{} {:02d}:{:02d}'.format(t[3], t[4], t[2], t[0], t[1]))


if __name__ == '__main__':
    main()
