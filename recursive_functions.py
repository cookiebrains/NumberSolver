from itertools import permutations
import pprint

OPERATIONS = ['add', 'sub', 'mul', 'div']



def _get_groupings(number_list):
    if len(number_list) == 1:
        yield number_list == [0]
    elif len(number_list) == 2:
        yield number_list
    else:
        yield from (
            (xx, yy)
            for i in range(1, len(number_list))
            for xx in _get_groupings(number_list[:i])
            for yy in _get_groupings(number_list[i:])
        )

def get_groupings(perms):
    for nums in perms:
        yield from _get_groupings(nums)


def two_digit_list(number_list):
    perms = permutations(number_list, 2)
    return perms

def two_digit_candidates(number_list):
    x, y = number_list[0], number_list[1]
        for name in OPERATIONS:
            yield name, x, y

def three_digit_candidates(number_list):
    x, y = number_list[0], number_list[1]
    if not isinstance(x, tuple) and not isinstance(y, tuple):
        for name in OPERATIONS:
            yield name, x, y


a = get_groupings([4, 6, 7, 4, 9])
for i in a:
    print(i)

