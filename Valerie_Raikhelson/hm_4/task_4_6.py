from collections import Counter

numbers = [1, 5, 2, 9, 2, 9, 1]
el_count = Counter(numbers)

for num, count in el_count.items():
    if count == min(el_count.values()):
        print(num)
