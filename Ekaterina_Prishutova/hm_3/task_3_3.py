test_string = "Ivanou Ivan"
split_test_string = test_string.split(" ")
split_test_string[0], split_test_string[1] = split_test_string[1], split_test_string[0]
test_string = ' '.join(split_test_string)
print(test_string)
