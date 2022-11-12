def reshape_v3(list_with_numbers, width, length):
    result_list = []
    counter = 0

    while counter <= width - 1:
        counter += 1
        result_list.append(list_with_numbers[:length])
        list_with_numbers = list_with_numbers[length:]
    print(result_list)


reshape_v3([1, 2, 3, 4, 5, 6], 2, 3)
reshape_v3([1, 2, 3, 4, 5, 6, 7, 8], 4, 2)


def positive_number_v2(list_with_numbers):
    result_list = [i for i in list_with_numbers if i > 0]
    print(result_list)


positive_number_v2([34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7])


def count_letters(sentence):
    gen_str = [i for i in sentence.split() if i != 'the']
    print(gen_str)


sentence = 'thequick brown fox jumps over the lazy dog'
count_letters(sentence)
