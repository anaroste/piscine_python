def main():
    t = (19, 42, 21, 56)
    buffer = f"The {len(t)} numbers are:"
    for elt in t:
        buffer += f" {elt},"
    print(buffer[:len(buffer) - 1])


if __name__ == '__main__':
    main()
