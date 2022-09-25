test_string = 'Ivan Ivanou'
test_string = test_string.split()
test_string.reverse()
# А вот тут хочется задать вопрос: почему не работает, если написать test_string = test_string.reverse()?
# Хотя со split() присвоение работает
print(test_string)
