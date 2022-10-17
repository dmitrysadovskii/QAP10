# @typed(type = str)
# def add_two_symbols(a, b):
#     return a + b


def decorator_maker_with_arguments(arg1, arg2):
    print(arg1, arg2)
    def typed(func):
        print(arg1, arg2)
        def wrapper(func_arg1, func_arg2):
            print(arg1, arg2, func_arg1, func_arg2)


        return wrapper
    return typed


    @typed(type = str)
    def summa(a, b):
        print(a+b)


    summa(1, 2)
