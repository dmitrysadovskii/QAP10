for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, 'FuzzBuzz')
    elif i % 3 == 0:
        print(i, 'Fuzz')
    elif i % 5 == 0:
        print(i, 'Buzz')
    else:
        print(i)
