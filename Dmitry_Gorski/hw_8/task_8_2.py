num_dict = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
            9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
            16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}


def check_args(*args):
    assert (isinstance(arg, (int, float)) for arg in args), 'All args must be int or float'
    assert (0 <= arg < 20 for arg in args), 'All args must be in range [0; 20)'
    assert len(args) <= 100, 'The total number of args must not gt 100'


def lexicographic_sort(*args):
    check_args(args)
    return list(dict(sorted([(v, k) for k, v in
                             {k: v for k, v in num_dict.items() for arg in args if arg == k}.items()])).values())


print(lexicographic_sort(1, 2, 3))
