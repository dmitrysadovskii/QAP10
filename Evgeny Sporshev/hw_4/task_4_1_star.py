from collections import Counter

test_list = [1, 5, 2, 9, 2, 9, 1]

test_list_counter = Counter(test_list)
print(test_list_counter)

for k, v in test_list_counter.items():
    if v == 1:
        print(k)
