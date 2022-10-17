def decorator(func_for_decorate):
    def wrapper(string):
        number_names = {
            0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
            9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
            16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
        input_list = string.split(" ")
        for i in range(len(input_list) - 1, -1, -1):
            for j in range(i):
                if number_names[int(input_list[j])] > number_names[int(input_list[j + 1])]:
                    input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
        func_for_decorate(" ".join(input_list))

    return wrapper


@decorator
def func(string):
    print(string)


func("1 2 3 4 5 2 19 3 4 1 2 0 15")
