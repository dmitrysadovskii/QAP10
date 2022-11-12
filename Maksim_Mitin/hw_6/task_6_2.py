def counting_occurrences(string):
    string_to_list = list(string)
    counter_list = []

    for let in string_to_list:
        if let not in counter_list:
            counter_list.append(let)

    string_result = ""

    for letter in counter_list:
        if string.count(letter) == 1:
            string_result += letter
        else:
            string_result += letter + str(string.count(letter))
    return string_result


print(counting_occurrences("cccbba"))
print(counting_occurrences("abeehhhhhccced"))
print(counting_occurrences("aaabbceedd"))
