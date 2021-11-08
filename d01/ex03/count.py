def text_analyzer(*text):
    """This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text."""
    upper = 0
    lower = 0
    punct = 0
    space = 0

    if len(text) > 1:
        print('ERROR')
        return

    if len(text) == 0:
        text = input('What is the text to analyse?\n>>')

    for caract in text[0]:
        if caract.isalpha():
            if caract.isupper():
                upper += 1
            else:
                lower += 1
        elif caract.isspace():
            space += 1
        elif not caract.isnumeric():
            punct += 1
    print(f"The text contains {len(text[0])} characters:\n"
          f"- {upper} upper letters\n"
          f"- {lower} lower letters\n"
          f"- {punct} punctuation marks\n"
          f"- {space} spaces")
