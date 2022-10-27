def typed(type_input):
    def decorator(func_for_decorate):
        def wrapper(*args):
            input_list = []
            for val in args:
                input_list.append(type_input(val))
            return func_for_decorate(*input_list)
        return wrapper
    return decorator


@typed(type_input=str)
def add_two_symbols(a, b):
    return a + b


@typed(type_input=int)
def add_three_symbols(a, b, c):
    return a + b + с


print(add_two_symbols(1, 2))
print(add_three_symbols(1, 2, 3))
