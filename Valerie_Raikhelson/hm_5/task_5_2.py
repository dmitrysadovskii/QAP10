for number in range(1, 100):
    if number % 3 == 0:
        print("Fuzz")
        continue
    if number % 5 == 0:
        print("Buzz")
        continue
    if number % 3 == 0 and number % 5 == 0:
        print("FuzzBuzz")
        continue
    if print(number):
        pass
