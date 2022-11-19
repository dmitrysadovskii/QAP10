# генераторы 2:
sentence = " thequick brown fox jumps over the lazy dog"


def exclude_the(text):
    return [len(x) for x in text.split() if text != 'the']


print(exclude_the(sentence))
