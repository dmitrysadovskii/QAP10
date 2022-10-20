import collections


information = input("Введите данные для подсчета: ")


def repetition_calculus(letters: str) -> str:
    counting_dict = dict(collections.Counter(letters))
    dictionary = []
    for key, value in counting_dict.items():
        if value == 1:
            dictionary.append(f'{key}{""}')
        else:
            dictionary.append(f'{key}{value}')

    return "".join(dictionary)


print(repetition_calculus(information))
