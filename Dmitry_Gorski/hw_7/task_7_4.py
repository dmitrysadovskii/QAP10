def cesar_coding(in_str: str, bias: int, lang='eng') -> str:
    assert lang in ('eng', 'rus'), 'You can use only ENG|RUS language'

    out_string = str()
    if lang == 'eng':
        upper_letter, lower_letter = 'A', 'a'
        amount_letter = 26
    else:
        upper_letter, lower_letter = 'А', 'а'
        amount_letter = 32

    for i in in_str:
        if i.isupper():
            out_string += \
                chr((ord(i) - ord(upper_letter) + bias) % amount_letter +
                    ord(upper_letter))
        elif i.islower():
            out_string += \
                chr((ord(i) - ord(lower_letter) + bias) % amount_letter +
                    ord(lower_letter))
        elif i.isdigit():
            out_string += str((int(i) + bias) % 10)
        else:
            out_string += i
    return out_string


print(cesar_coding('Hello World!', 4, 'eng'))
print(cesar_coding('Привет Мир!', 4, 'rus'))


def cesar_decoding(in_str: str, bias: int, lang='eng') -> str:
    assert lang in ('eng', 'rus'), 'You can use only ENG|RUS language'

    out_string = str()
    if lang == 'eng':
        upper_letter, lower_letter = 'A', 'a'
        amount_letter = 26
    else:
        upper_letter, lower_letter = 'А', 'а'
        amount_letter = 32

    for i in in_str:
        if i.isupper():
            out_string += \
                chr((ord(i) - ord(upper_letter) - bias) % amount_letter +
                    ord(upper_letter))
        elif i.islower():
            out_string += \
                chr((ord(i) - ord(lower_letter) - bias) % amount_letter +
                    ord(lower_letter))
        elif i.isdigit():
            out_string += str((int(i) - bias) % 10)
        else:
            out_string += i
    return out_string


print(cesar_decoding('Lipps Asvph!', 4, 'eng'))
print(cesar_decoding('Уфмжйц Рмф!', 4, 'rus'))


# Try make Two-in-one using OOP

class CesarCodeDecode:

    def __init__(self, str_in, bias, lang):
        self.str_in = str_in
        self.bias = bias
        self.lang = lang

    def coding(self):
        assert self.lang in ('eng', 'rus'), 'You can use only ENG|RUS language'

        if self.lang == 'eng':
            upper, lower = 'A', 'a'
            amount = 26
        else:
            upper, lower = 'А', 'а'
            amount = 32

        out_string = str()
        for i in self.str_in:
            if i.isupper():
                out_string += \
                    chr((ord(i) - ord(upper) + self.bias) % amount +
                        ord(upper))
            elif i.islower():
                out_string += \
                    chr((ord(i) - ord(lower) + self.bias) % amount +
                        ord(lower))
            elif i.isdigit():
                out_string += str((int(i) + self.bias) % 10)
            else:
                out_string += i
        return out_string

    def decoding(self):
        self.bias = - self.bias
        out_string = self.coding()
        return out_string


print(CesarCodeDecode('Hello World!', 4, 'eng').coding())
print(CesarCodeDecode('Привет Мир!', 4, 'rus').coding())
print(CesarCodeDecode('Lipps Asvph!', 4, 'eng').decoding())
print(CesarCodeDecode('Уфмжйц Рмф!', 4, 'rus').decoding())
