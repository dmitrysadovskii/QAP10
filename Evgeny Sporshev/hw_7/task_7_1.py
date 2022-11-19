def reshape(number_list, width, length):
    number_list = iter(number_list)
    result = []

    for width_list in range(width):
        width_list = list()
        for i in range(length):
            width_list.append(next(number_list))
        result.append(width_list)
    return result


print(reshape([1, 2, 3, 4, 5, 6], 2, 3))
print(reshape([1, 2, 3, 4, 5, 6, 7, 8], 4, 2))
