print('enter a word with leading and trailing whitespaces')
demo = input()
remove_whitespaces = demo.lstrip().rstrip()
print(remove_whitespaces)