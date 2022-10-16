import random

secret_number = '2314'

while True:
    bulls = 0
    cows = 0
    input_number = input("Enter a 4-digit number with non-repetitive digits: ")
    if len(input_number) != 4:
        print("Enter a 4-digit number")
        continue
    elif len(set(input_number)) != 4:
        print("Enter non-repetitive digits")
        continue
    for i in range(4):
        if secret_number[i] == input_number[i]:
            bulls += 1
        elif input_number[i] in secret_number:
            cows += 1
    print(str(bulls) + ' bull and ' + str(cows) + ' cows')
    if bulls == 4:
        print("You won!")
        break