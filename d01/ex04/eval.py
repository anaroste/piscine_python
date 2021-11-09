def check(words, coefs):
    if not isinstance(words, list) and not isinstance(coefs, list):
        return False
    if len(coefs) != len(words):
        return False
    for elt in words:
        if not isinstance(elt, str):
            print(elt)
            return False
    for elt in coefs:
        if not isinstance(elt, float) and not isinstance(elt, int):
            return False
    return True


class Evaluator:
    def __init__(self, words, coefs):
        if not check(coefs, words):
            return -1
        self.words = words
        self.coefs = coefs

    def zip_evaluate(coefs, words):
        if not check(words, coefs):
            return -1
        tab = zip(words, coefs)
        ret = 0
        for elt in tab:
            ret += len(elt[0]) * elt[1]
        return ret

    def enumerate_evaluate(coefs, words):
        if not check(words, coefs):
            return -1
        tab = enumerate(words)
        ret = 0
        for elt in tab:
            ret += len(elt[1]) * coefs[elt[0]]
        return ret
