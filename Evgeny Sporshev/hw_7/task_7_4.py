# Шифр цезаря
alphabet = 'abcdefghijklmnopqrstuvwxyz'
example_one = 'hello world!'
example_two = 'this is a test string'


def encode(some_string, step):
    result = ''
    for i in some_string:
        if i in alphabet:
            position = alphabet.find(i)
            new_pos = alphabet[position + step]
            result += new_pos
        else:
            result += i
    return result


def decode(some_string, step):
    result = ''
    for i in some_string:
        if i in alphabet:
            position = alphabet.find(i)
            new_pos = alphabet[position - step]
            result += new_pos
        else:
            result += i
    return result


action_one = encode(example_one, 1)
print(f'Результат кодирования строки {example_one} : {action_one}')
action_two = decode(action_one, 1)
print(f'Результат декодирования строки {action_one} : {action_two}')

action_one = encode(example_two, 1)
print(f'Результат кодирования строки {example_two} : {action_one}')
action_two = decode(action_one, 1)
print(f'Результат декодирования строки {action_one} : {action_two}')
