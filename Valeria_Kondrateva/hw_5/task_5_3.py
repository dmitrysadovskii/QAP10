a = [1, 2, 3, 4]  # Загаданное число

while True:

    cow = 0
    bull = 0

    number = input('Введите 4-значное число ')

    b = [int(x) for x in str(number)]

    for i in range(len(a)):
        if a[i] in b:
            cow += 1

        if a[i] == b[i]:
            bull += 1

    cow -= bull

    if bull == 4:
        break
    else:
        dct_cow = {0: 'Коров нет', 1: 'Одна корова', 2: 'Двe коровы', 3: 'Три коровы', 4: 'Четыре коровы'}
        dct_bull = {0: 'Быков нет', 1: 'Один бык', 2: 'Два быка', 3: 'Три быка'}

        print(f"{dct_cow[cow]}, {dct_bull[bull]}.\n")


print("Вы выиграли!")
