text_to_encode = input('Введите текст для шифрования: ')
letters = 'abcdefghijklmnopqrstuvwxyz'


def encode(some_text):
    step = int(input('Введите шаг кодировки: '))
    result = ''
    for element in some_text.lower():
        pos_now = letters.find(element)
        position2 = pos_now + step
        if element in letters:
            result += letters[position2]
        else:
            result += element
    return result


print(encode(text_to_encode))
text_to_decode = input('Введите зашифрованый текст: ')


def decode(some_text):
    step = int(input('Введите шаг кодировки: '))
    result = ''
    for element in some_text.lower():
        pos_now = letters.find(element)
        position2 = pos_now - step
        if element in letters:
            result += letters[position2]
        else:
            result += element
    return result


print(decode(text_to_decode))
