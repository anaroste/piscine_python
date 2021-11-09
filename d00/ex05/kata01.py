def main():
    languages = {
        'Python': 'Guido van Rossum',
        'Ruby': 'Yukihiro Matsumoto',
        'PHP': 'Rasmus Lerdorf',
    }

    for key, value in languages.items():
        print(f"{key} was created by {value}")


if __name__ == '__main__':
    main()
