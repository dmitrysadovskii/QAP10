original_text = "Be happy"
decoded_text = ""


def encode(text, key):
    encrypted = ""
    for letter in text:
        if letter.isupper():
            letter_index = ord(letter) - ord('A')
            letter_shifted = (letter_index + key) % 26 + ord('A')
            letter_new = chr(letter_shifted)
            encrypted += letter_new
        elif letter.islower():
            letter_index = ord(letter) - ord('a')
            letter_shifted = (letter_index + key) % 26 + ord('a')
            letter_new = chr(letter_shifted)
            encrypted += letter_new
        elif letter.isdigit():
            letter_new = (int(letter) + key) % 10
            encrypted += str(letter_new)
        else:
            encrypted += letter
    return encrypted


def decode(text, key):
    decrypted = ""
    for letter in text:
        if letter.isupper():
            letter_index = ord(letter) - ord('A')
            letter_og_pos = (letter_index - key) % 26 + ord('A')
            letter_og = chr(letter_og_pos)
            decrypted += letter_og
        elif letter.islower():
            letter_index = ord(letter) - ord('a')
            letter_og_pos = (letter_index - key) % 26 + ord('a')
            letter_og = chr(letter_og_pos)
            decrypted += letter_og
        elif letter.isdigit():
            letter_og = (int(letter) - key) % 10
            decrypted += str(letter_og)
        else:
            decrypted += letter
    return decrypted


print(encode(original_text, 5))
print(decode(decoded_text, 5))
