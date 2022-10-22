alphabet = "abcdefghijklmnopqrstuvwxyz"


def decode(encrypted_string, shift_number):
    encrypted_string = encrypted_string.lower()
    string_befor_encrypt = ""

    for letter in encrypted_string:
        if letter in alphabet:
            string_befor_encrypt += alphabet[alphabet.index(letter) - shift_number]
        else:
            string_befor_encrypt += letter

    return string_befor_encrypt


def encode(string_befor_encrypt: str, shift_number: int):

    string_befor_encrypt = string_befor_encrypt.lower()
    encrypted_string = str()

    for letter in string_befor_encrypt:
        if letter in alphabet:
            encrypted_string += alphabet[(alphabet.index(letter) + shift_number) % len(alphabet)]
        else:
            encrypted_string += letter

    return encrypted_string


print(encode("hello world!", 3))
print(decode("khoor zruog!", 3))
