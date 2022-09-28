from collections import Counter
numbers = Counter([1, 5, 2, 9, 2, 9, 1])
print(numbers)
print(min(numbers, key=numbers.get))
