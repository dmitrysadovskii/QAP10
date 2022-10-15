number = input('Введите 4 значное число без повторных цифр - ')

if len(number) != 4:
    print("введено неправлиьное число, введено больше или меньше 4 чисел")
    number = input('Введите 4 значное число без повторных цифр - ')

list_check = [int(n) for n in number]
uniquelist = []

for item in list_check:
    itemExist = False
    for x in uniquelist:
        if x == item:
            itemExist = True
            print("введено неправлиьное число, числа повторяются")
            number = input('Введите 4 значное число без повторных цифр - ')
    if not itemExist:
        uniquelist.append(item)


def cows_and_bulls(some_numbers):
    listnumbers = [int(n) for n in some_numbers]
    while True:
        print(f"Загадано число {str(listnumbers)}")
        guess = [int(i) for i in str(input())]

        if guess == listnumbers:
            print("Вы выиграли")
            break
        else:
            cow = 0
            bull = 0

            for x in range(len(listnumbers)):
                if guess[x] == listnumbers[x]:
                    bull += 1
                elif guess[x] in listnumbers:
                    cow += 1
                else:
                    continue

        print(f"Коров = {str(cow)}. Быков = {str(bull)}")


cows_and_bulls(number)
