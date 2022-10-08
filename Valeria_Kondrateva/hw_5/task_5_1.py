names = ["Ann", "Alex", "Mark", "Max"]
a = len(names)
if a == 0:
    print('no one likes this')
elif a == 1:
    print(f'{names[0]} likes this')
elif a == 2:
    print(f'{names[0]} and {names[1]} likes this')
elif a == 3:
    print(f'{names[0]}, {names[1]} and {names[2]} likes this')
else:

    print(f'{names[0]}, {names[1]} and {a - 2} others likes this')
