card_number_text = input("Введите номер кредитной карты для валидации: ")
check_letters = 'qwertyuiopasdfghjklzxcvbnm' \
                'цукенгшщзхъёфывапролджэячсмитьбю <>?/[]{}-=+!@#$%^&*()\\\'\"'


def check_string():
    for letter in card_number_text:
        if letter in check_letters:
            return False
        else:
            return True


def luhn_checksum(card_number):
    if check_string():
        def digits_of(n):
            return [int(d) for d in str(n)]

        digits = digits_of(card_number)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = 0
        checksum += sum(odd_digits)
        for d in even_digits:
            checksum += sum(digits_of(d * 2))
        return checksum % 10
    else:
        print("Введен запрещенный символ !!!")


print('True') if luhn_checksum(card_number_text) == 0 else print('False')
