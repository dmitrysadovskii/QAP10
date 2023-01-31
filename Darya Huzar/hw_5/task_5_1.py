import langid

names = input("Введите имена/Enter names: ")
array = names.split()
array_lang = langid.classify(names)


def en_names():
    if len(array) == 0:
        print("no one likes this")
    elif len(array) == 1:
        print(array[0], "likes this")
    elif len(array) == 2:
        print(array[0], "and", array[1], "like this")
    elif len(array) == 3:
        print(array[0], array[1], "and", array[2], "like this")
    elif len(array) > 3:
        print(array[0], array[1], "and", len(array) - 2, "others like this")


def ru_names():
    if len(array) == 0:
        print("это никому не нравится")
    elif len(array) == 1:
        print(array[0], "нравится это")
    elif len(array) == 2:
        print(array[0], "и", array[1], "нравится это")
    elif len(array) == 3:
        print(array[0], array[1], "и", array[2], "нравится это")
    elif len(array) > 3:
        print(array[0], array[1], "и", len(array) - 2, "другим нравится это")


if array_lang[0] == 'en':
    en_names()
elif array_lang[0] == 'ru':
    ru_names()
else:
    print("Invalid language")
