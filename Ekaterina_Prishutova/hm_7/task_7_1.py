def func_var_1(input_list, length, width):
    if len(input_list) is not length * width:
        print("Неверно заданы размеры")
        return None
    else:
        return_matrix = []
        for inc in range(width):
            return_matrix.append([])
        for value in enumerate(input_list):
            return_matrix[int(value[0] / length)].append(value[1])
        return return_matrix


def func_var_2(input_list, length, width):
    if len(input_list) is not length * width:
        print("Неверно заданы размеры")
        return None
    else:
        return [input_list[i:i + length] for i in range(0, len(input_list), length)]


print(func_var_1([1, 2, 3, 4, 5, 6], 2, 3))
print(func_var_2([1, 2, 3, 4, 5, 6], 2, 3))
