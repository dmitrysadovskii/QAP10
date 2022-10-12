def luhn(card):

    checksum = 0
    cardnums = list(map(int, card))

    for count, num in enumerate(cardnums):

        if count % 2 == 0:
            buffer = num * 2

            if buffer > 9:
                buffer -= 9

            checksum += buffer

        else:
            checksum += num

    return checksum % 10 == 0


print(luhn('378282246310005'))
