# enter a string in the console
old_str = input()
new_str = ' '.join(f'{word}ing' for word in old_str.split())
print(new_str)
