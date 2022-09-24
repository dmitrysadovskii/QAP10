string = "Hello world"

characters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x',
              'c', 'v', 'b', 'n', 'm']


def findCharacters(some_string):
    some_string.lower()
    text = some_string.replace(" ", "")
    d = {}
    for t in text:
        if t in characters:
            d[t] = text.count(t)
    m = max(d.values())
    cont = m
    l = []
    for key in d:
        if d[key] == cont:
            l.append(key)
    print(l)


findCharacters(string)
