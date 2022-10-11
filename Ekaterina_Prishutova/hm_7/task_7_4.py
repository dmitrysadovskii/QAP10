import random


def caesar_wrapper(input_string, num, mode, language):
    if mode == "encode":
        return caesar(input_string, num, language)
    elif mode == "decode":
        return caesar(input_string, -num, language)
    else:
        print("Некорректно выбран режим кодирования")
        return None


def caesar(input_string, num, language):
    if language == "en":
        abc = "".join([chr(letter) for letter in range(ord("a"), ord("z") + 1)] +
                      [chr(letter) for letter in range(ord("A"), ord("Z") + 1)])
    elif language == "ru":
        abc = "".join([chr(letter) for letter in range(ord("а"), ord("е") + 1)]) + chr(ord("ё")) + \
              "".join([chr(letter) for letter in range(ord("ж"), ord("я") + 1)]) + \
              "".join([chr(letter) for letter in range(ord("А"), ord("Е") + 1)]) + chr(ord("Ё")) + \
              "".join([chr(letter) for letter in range(ord("Ж"), ord("Я") + 1)])
    else:
        print("Неподдерживаемый язык")
        return
    return "".join([abc[(abc.index(el) + num % len(abc)) % len(abc)]
                    if abc.find(el) >= 0 else el for el in input_string])


def kati_encode(input_string, mode, language):
    if language == "en":
        abc = "".join([chr(letter) for letter in range(ord("a"), ord("z") + 1)] +
                      [chr(letter) for letter in range(ord("A"), ord("Z") + 1)])
    elif language == "ru":
        abc = "".join([chr(letter) for letter in range(ord("а"), ord("е") + 1)]) + chr(ord("ё")) + \
              "".join([chr(letter) for letter in range(ord("ж"), ord("я") + 1)]) + \
              "".join([chr(letter) for letter in range(ord("А"), ord("Е") + 1)]) + chr(ord("Ё")) + \
              "".join([chr(letter) for letter in range(ord("Ж"), ord("Я") + 1)])
    else:
        print("Неподдерживаемый язык")
        return
    if mode == "encode":
        num = (len(input_string) % len(abc) + int(len(abc) / 4)) % len(abc)
        return "".join([abc[(abc.index(el) + num % len(abc)) % len(abc)] + chr(random.randrange(ord("a"), ord("z") + 1))
                        if abc.find(el) >= 0 else el + chr(random.randrange(ord("a"), ord("z") + 1))
                        for el in input_string[::-1]])
    elif mode == "decode":
        num = -(int(len(input_string) / 2) % len(abc) + int(len(abc) / 4)) % len(abc)
        return "".join([abc[(abc.index(el) + num % len(abc)) % len(abc)]
                        if abc.find(el) >= 0 else el
                        for el in input_string[-2::-2]])
    else:
        print("Некорректно выбран режим кодирования")
        return


in_str_en = "th!is IS a teSt ]6stri()ng"
in_str_ru = "Ехал Гpека чеpез pеку, видит Гpека – в pеке pак. Сунул Гpека pуку в pеку, pак за pуку Гpеку цап!"

print("Caesar en")
print(in_str_en)
st_1 = caesar_wrapper(in_str_en, 3, "encode", "en")
print(st_1)
print(caesar_wrapper(st_1, 3, "decode", "en"))

print("Caesar ru")
print(in_str_ru)
st_2 = caesar_wrapper(in_str_ru, 3, "encode", "ru")
print(st_2)
print(caesar_wrapper(st_2, 3, "decode", "ru"))

print("kati en")
print(in_str_en)
st_3 = kati_encode(in_str_en, "encode", "en")
print(st_3)
print(kati_encode(st_3, "decode", "en"))

print("kati ru")
print(in_str_ru)
st_4 = kati_encode(in_str_ru, "encode", "ru")
print(st_4)
print(kati_encode(st_4, "decode", "ru"))
