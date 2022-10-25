def typed(type_symbol):
    def decorator(func_to_decorate):
        def wrapper(*args):
            new_args = []
            if type_symbol == 'str':
                for sym in args:
                    new_args.append(str(sym))
            elif type_symbol == 'int':
                for sym in args:
                    if type(sym) == float:
                        new_args.append(float(sym))
                    else:
                        new_args.append(int(sym))
            return func_to_decorate(*new_args)
        return wrapper
    return decorator


@typed(type_symbol='str')
def add_two_symbols(a, b):
    return a + b


@typed(type_symbol='int')
def add_three_symbols(a, b, c):
    return a + b + c


print(add_two_symbols("3", 5))
print(add_two_symbols(5, 5))
print(add_two_symbols('a', 'b'))
print(add_three_symbols(5, 6, 7))
print(add_three_symbols("3", 5, 0))
print(add_three_symbols(0.1, 0.2, 0.4))
