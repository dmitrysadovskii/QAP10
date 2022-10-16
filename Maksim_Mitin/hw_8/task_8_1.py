def typed(type):
    def decorator_function(wrapped_func):
        def wrapper(*args):
            if type == 'str':
                result = ""
                return result.join(str(value) for value in args)
            elif type == 'int':
                result = 0
                for i in args:
                    if isinstance(i, float):
                        result += float(i)
                    elif isinstance(i, int):
                        result += int(i)
                return result
        return wrapper
    return decorator_function


@typed(type='str')
def add_two_symbols(a, b):
    return a + b


@typed(type='int')
def add_three_symbols(a, b, c):
    return a + b + c


result = add_two_symbols("3", 5)
print(result)
result = add_two_symbols('a', 'b')
print(result)
result = add_three_symbols(5, 6, 7)
print(result)
result = add_three_symbols("3", 5, 0)
print(result)
result = add_three_symbols(0.1, 0.2, 0.4)
print(result)
