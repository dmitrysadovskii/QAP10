original_str = [1, 2, 3, 4]
win_flag = 1
while win_flag:
    bull = 0
    cow = 0
    input_str = input("Введите число: ")
    if not input_str.isdigit() or len(input_str) != len(original_str):
        print("Некорректный ввод числа")
        break
    input_list = list(map(int, input_str))
    for i in range(len(original_str)):
        for j in range(len(original_str)):
            if original_str[i] == input_list[j]:
                if i == j:
                    bull += 1
                else:
                    cow += 1
    print(f"Количество быков: {bull},количество коров: {cow}")
    if bull == 4:
        print("WIN")
        win_flag = 0
