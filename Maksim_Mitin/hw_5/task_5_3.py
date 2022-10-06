import random
# делал через генерацию рандомных чисел, по идее можно через инпут запрашивать число и его аргументом в функцию
# (но там надо проверки делать на кратность4 и без симвлов и букв,я подумал надо сделать просто)


def cows_and_bulls():
    listnumbers = [random.randint(0, 9) for n in range(4)]

    while True:
        print(f"Загадано число {str(listnumbers)}")
        guess = [int(i) for i in str(input())]

        if guess == listnumbers:
            print("Вы выиграли")
            break
        else:
            cow = 0
            bull = 0

            for x in range(0, 3):
                if guess[x] == listnumbers[x]:
                    cow += 1
                elif guess[x] in listnumbers:
                    bull += 1
        print(f"Коров = {str(cow)}. Быков = {str(bull)}")


cows_and_bulls()
