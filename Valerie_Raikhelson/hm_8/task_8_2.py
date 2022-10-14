from num2words import num2words


def input_numbers():
    numbers = []
    amount = int(input("How many numbers will be entered? "))
    while len(numbers) < amount:
        if amount < 100:
            num = int(input("Enter number: "))
        if 0 < num < 19:
            numbers.append(num)
        else:
            print("The entered number should be greater than 0 and less than 19")
    return numbers


def number_in_words():
    d = {}
    for num in input_numbers():
        d[num] = num2words(num, to='ordinal')
    return dict(sorted(d.items(), key=lambda item: item[1]))


def get_numbers_sorted_by_lexicographical_increase():
    return list(number_in_words().keys())


print(get_numbers_sorted_by_lexicographical_increase())
