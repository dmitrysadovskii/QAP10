check_string = "aaahhggggrearrrkk"


def letter_count(check_str):
    count_let = 1
    result = ''
    for key, _ in enumerate(check_str):
        if key == len(check_str) - 1:
            if count_let == 1:
                result += check_str[key]
            else:
                result += check_str[key] + str(count_let)
            break
        if check_str[key] == check_str[key + 1]:
            count_let += 1
        else:
            if count_let == 1:
                result += check_str[key]
            else:
                result += check_str[key] + str(count_let)
            count_let = 1
    return result


print(letter_count(check_string))
