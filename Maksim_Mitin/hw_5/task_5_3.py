import random

def cows_and_bulls(digits):
    listnumbers = [random.randint(0, 9) for n in range(digits)]
    count = 0

    while True:
        count += 1
        print(f"Попытка № {str(count)}" )
        print(f"Подсказка для теста {str(listnumbers)}")

        print(f"Угадай  {str(digits)} значное число")
        guess = [int(i) for i in str(input())]

        if guess == listnumbers:
            print("Вы выиграли")
            break
        else:
            cow = 0
            bull = 0

            for x in range(0, digits):
                if guess[x]==listnumbers[x]:
                    cow += 1
                elif guess[x] in listnumbers:
                    bull += 1

        print(f"Коров = {str(cow)}. Быков = {str(bull)}")

cows_and_bulls(4)