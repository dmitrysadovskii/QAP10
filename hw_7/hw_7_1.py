def typed(type):
    def decorator(func):
        def wrapper(*args):
            s = []
            if type == 'str':
                for i in args:
                    s.append(str(i))
            elif type == 'int':
                for i in args:
                    s.append(int(i))
            else:
                for i in args:
                    s.append(float(i))
            return func(*s)

        return wrapper

    return decorator


@typed(type='str')
def add_two_symbols(a, b):
    return a + b


@typed(type='int')
def add_three_symbols(a, b, c):
    return a + b + c


@typed(type='float')
def add_float_symbols(a, b, c):
    return a + b + c


print(add_two_symbols("3", 5))
print(add_two_symbols(5, 5))
print(add_two_symbols('a', 'b'))
print(add_three_symbols(5, 6, 7))
print(add_three_symbols("3", 5, 0))
print(add_float_symbols(0.1, 0.2, 0.4))
