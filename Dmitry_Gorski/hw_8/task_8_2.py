numbers = [x for x in range(20)]
number_names = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
                'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']


def check_args(*args):
    assert (isinstance(arg, (int, float)) for arg in args), 'All args must be int or float'
    assert (0 <= arg < 20 for arg in args), 'All args must be in range [0; 20)'
    assert len(args) <= 100, f'The total number of args must not gt 100'


def lexicographic_sort(*args):
    check_args(args)
    return ', '.join(set(sorted([dict(zip(numbers, number_names)).get(arg) for arg in args])))


print(lexicographic_sort(1, 2, 3))