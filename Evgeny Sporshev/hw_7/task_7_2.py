# генераторы 1:
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]


def numbers_check(number_list):
    return [i for i in number_list if i >= 0]


print(numbers_check(numbers))
