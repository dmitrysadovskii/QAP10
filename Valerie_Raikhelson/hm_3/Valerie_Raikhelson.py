link = 'www.my_site.com#about'
print(link.replace('#', '/'))

print('enter a word:')
word = input()
print(word + 'ing')

name = 'Ivanou Ivan'
print(' '.join(name.split(' ')[::-1]))

print('enter a word with leading and trailing whitespaces')
demo = input()
remove_whitespaces = demo.lstrip().rstrip()
print(remove_whitespaces)
