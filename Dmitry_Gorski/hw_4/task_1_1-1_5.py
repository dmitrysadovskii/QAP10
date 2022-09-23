""" Перевести строку в массив Robin Singh = [Robin, Singh]
I love arrays they are my favorite = [I, love, arrays, they, are, my, favorite] """

s1, s2 = 'Robin Singh', 'I love arrays they are my favorite'
print(f'{s1.split(" ")}\n{s2.split(" ")}')


""" Дан список: [‘Ivan’, ‘Ivanou’], и 2 строки: Minsk, Belarus
Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus” """

lst, s1, s2 = ['Ivan', 'Ivanou'], 'Minsk', 'Belarus'
print(f'Привет, {" ".join(lst)}! Добро пожаловать в {s1} {s2}')


""" Дан список ['I', 'love', 'arrays', 'they', 'are', 'my', 'favorite'] сделайте из него
строку 'I love arrays they are my favorite' """

lst = ['I', 'love', 'arrays', 'they', 'are', 'my', 'favorite']
print(' '.join(lst))


""" Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
удалите элемент из списка под индексом 6 """

lst = [i for i in range(0, 10)]
lst.insert(3, -999)
lst.pop(6)
print(lst)


""" Есть 2 словаря a = { a: 1, b: 2, c: 3} b = { c: 3, d: 4, e: 5} 
Необходимо их объединить по ключам, а значения ключей поместить в список, если у одного словаря есть ключ
а, а у другого нету, то поставить значение None на соответствующую позицию(1-я позиция для 1-ого словаря,
вторая для 2-ого) ab = {a: [1, None], b: [2, None], c: [3, 3], d: [None, 4], e: [None, 5]} """

a, b, ab = {'a': 1, 'b': 2, 'c': 3}, {'c': 3, 'd': 4, 'e': 5}, {}

for k, v in {**a, **b}.items():
    if k in a and k in b:
        ab.update({k: [a[k], b[k]]})
    else:
        ab.update({k: [v, None]})
print(ab)
