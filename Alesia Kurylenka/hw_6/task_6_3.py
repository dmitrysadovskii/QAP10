user_input = input("Please choose the program and enter: \nfor Addition - add, \n"
                   "for Subtraction - sub, \nfor Multiplication - mul, \nfor Division - div: ")


def calculation():
    number1 = input("Please enter first number: ")
    number2 = input("Please enter second number: ")
    if number1.isdigit() and number2.isdigit():
        a = float(number1)
        b = float(number2)
        if user_input == "add":
            print(a + b)
        elif user_input == "sub":
            print(a - b)
        elif user_input == "mul":
            print(a * b)
        elif user_input == "div":
            if b == 0:
                print("division by 0 is not allowed")
            else:
                int_part = int(a // b)
                remainder = int(a % b)
                print(f"integer part of number: {int_part}, remainder of division: {remainder}")
    else:
        print("please enter digits only")


def program_input():
    if user_input not in ["add", 'sub', 'mul', 'div']:
        print("Enter valid operation")
    else:
        calculation()


program_input()
