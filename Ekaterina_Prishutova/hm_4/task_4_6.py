from collections import Counter
input_list = [1, 5, 2, 9, 2, 9, 1]
k, v = Counter(input_list).most_common()[-1]
print(f"Unique number: {k}")
