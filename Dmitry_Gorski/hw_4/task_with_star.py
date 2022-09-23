"""
Вам передан массив чисел. Известно, что каждое число в этом массиве имеет
пару, кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5
Напишите программу, которая будет выводить уникальное число
"""

from collections import Counter

print(''.join([str(k) for k, v in Counter([1, 5, 2, 9, 2, 9, 1]).items() if v == 1]))


"""Дан текст, который содержит различные английские буквы и знаки препинания. Вам необходимо найти самую частую букву
в тексте. Результатом должна быть буква в нижнем регистре. При поиске самой частой буквы, регистр не имеет значения,
так что при подсчете считайте, что A == a. Убедитесь, что вы не считайте знаки препинания, цифры и пробелы, а только
буквы.
Если в тексте две и больше буквы с одинаковой частотой, тогда результатом будет буква, которая идет первой в алфавите.
Для примера, one содержит o, n, e по одному разу, так что мы выбираем e."""

sample = 'shdf lsdfJKGTUYKKhFK"LKHaaaaaaksdnbnsafs?>>?<?></)(**^&%^!632328732  sdjfskdRFCNGKJB<M<MN'

d, lst = Counter(list(sample.replace(' ', '').lower())), []
for k, v in d.items():
    if v == max(d.values()) and k.isalpha():
        lst.append(k)

print(sorted(lst)[0])
