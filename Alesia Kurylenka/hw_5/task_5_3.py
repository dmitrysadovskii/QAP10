import random

# 1 case: game with person
number1 = input("Please enter a 4-digit number with non-repetitive digits: ")
while True:
    number2 = input("Please try to guess the secret number, enter a 4-digit number with non-repetitive digits: ")
    bulls = 0
    cows = 0
    for i in range(4):
        if number1[i] == number2[i]:
            bulls += 1
        elif number2[i] in number1:
            cows += 1
    print(str(bulls) + ' bull and ' + str(cows) + ' cows')
    if bulls == 4:
        print("you won the game!")
        break

# 2 case: game with computer

number_rand = random.sample("1234567890", 4)
number_rand_int = "".join(number_rand)
while True:
    number = input("Please try to guess the secret number, enter a 4-digit number with non-repetitive digits: ")
    bulls = 0
    cows = 0
    for i in range(4):
        if number[i] == number_rand_int[i]:
            bulls += 1
        elif number_rand_int[i] in number:
            cows += 1
    print(str(bulls) + ' bull and ' + str(cows) + ' cows')
    if bulls == 4:
        print("you won the game!")
        break
