def reshape(old_list: list, amount_list: int, len_list: int):
    result_list = []

    for index in range(amount_list):
        result_list.append(old_list[index * len_list:(index + 1) * len_list])

    return result_list


print(reshape([1, 2, 3, 4, 5, 6], 2, 3))
print(reshape([1, 2, 3, 4, 5, 6, 7, 8], 4, 2))
