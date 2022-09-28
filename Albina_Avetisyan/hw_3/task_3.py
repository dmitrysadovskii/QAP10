print('zadanie 1 =)')
expression = 'www.my_site.com#about'
print(expression.replace('#', '/'))

print('zadanie 2 =)')
expression = 'There is a great meme that sums it up'
print(expression.replace(' ', 'ing ') + "ing")

print('zadanie 3 =)')
expression = "Ivanou Ivan"
r = expression.split(' ')
r.reverse()
print(' '.join(r))

print('zadanie 4 =)')
expression = ' ' + expression + '  '
print(expression.strip())
