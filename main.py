import operator
from itertools import permutations

OPERATIONS = {
    "add": operator.add,
    "mul": operator.mul,
    "sub": operator.sub,
    "div": operator.truediv,
}

SYMBOLS = {
    "add": "+",
    "mul": "*",
    "sub": "-",
    "div": "/",
}


def _get_groupings(nums):
    if len(nums) == 1:
        yield nums[0]
    elif len(nums) == 2:
        yield nums
    else:
        yield from (
            (xx, yy)
            for i in range(1, len(nums))
            for xx in _get_groupings(nums[:i])
            for yy in _get_groupings(nums[i:])
        )


def get_groupings(perms):
    for nums in perms:
        yield from _get_groupings(nums)


def _generate_candidates(nums):
    x, y = nums[0], nums[1]
    if not isinstance(x, tuple) and not isinstance(y, tuple):
        for name in OPERATIONS:
            yield name, x, y
    else:
        x_gens = [x] if not isinstance(x, tuple) else _generate_candidates(x)
        y_gens = [y] if not isinstance(y, tuple) else _generate_candidates(y)
        yield from (
            (name, a, b) for a in x_gens for b in y_gens for name in OPERATIONS
        )


def generate_two_number_candidates(numbers):
    all_permutations = (
         permutations(numbers, 2)
    )

    for g in get_groupings(all_permutations):
        yield from _generate_candidates(g)


def generate_three_number_candidates(numbers):
    all_permutations = (
         permutations(numbers, 3)
    )

    for g in get_groupings(all_permutations):
        yield from _generate_candidates(g)


def generate_four_number_candidates(numbers):
    all_permutations = (
         permutations(numbers, 4)
    )

    for g in get_groupings(all_permutations):
        yield from _generate_candidates(g)


def generate_five_number_candidates(numbers):
    all_permutations = (
         permutations(numbers, 5)
    )

    for g in get_groupings(all_permutations):
        yield from _generate_candidates(g)


def generate_six_number_candidates(numbers):
    all_permutations = (
         permutations(numbers, 6)
    )

    for g in get_groupings(all_permutations):
        yield from _generate_candidates(g)


def compute(candidate):
    name, x, y = candidate
    child_x, child_y = x, y
    child_x = compute(x)[1] if isinstance(x, tuple) else x
    child_y = compute(y)[1] if isinstance(y, tuple) else y
    return candidate, OPERATIONS[name](child_x, child_y)


def get_solutions(candidates, final_result):
    for candidate in candidates:
        try:
            n, r = compute(candidate)
        except (ValueError, ZeroDivisionError, TypeError, OverflowError):
            continue
        if r == final_result:
            yield r, n


def parse(candidate, bracket=True):
    name, x, y = candidate
    symbol = SYMBOLS[name]
    child_x = parse(x) if isinstance(x, tuple) else str(x)
    child_y = parse(y) if isinstance(y, tuple) else str(y)
    result = f" {symbol} ".join([child_x, child_y])
    if bracket:
        return f"({result})"
    return result


if __name__ == "__main__":
    target = int(input("Enter Target Number: "))
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    num3 = int(input("Enter Third Number: "))
    num4 = int(input("Enter Fourth Number: "))
    num5 = int(input("Enter Fifth Number: "))
    num6 = int(input("Enter Sixth Number: "))

    input_numbers = (num1, num2, num3, num4, num5, num6)
    index2 = 0
    index3 = 0
    index4 = 0
    index5 = 0
    index6 = 0

    print('Two number solutions:')
    for (x, y) in get_solutions(generate_two_number_candidates(input_numbers), target):
        expr = parse(y, False)
        print(f"{expr} = {x}")
        index2 += 1
        if index2 == 4:
            break

    print('Three number solutions:')
    for (x, y) in get_solutions(generate_three_number_candidates(input_numbers), target):
        expr = parse(y, False)
        print(f"{expr} = {x}")
        index3 += 1
        if index3 == 4:
            break

    print('Four number solutions:')
    for (x, y) in get_solutions(generate_four_number_candidates(input_numbers), target):
        expr = parse(y, False)
        print(f"{expr} = {x}")
        index4 += 1
        if index4 == 4:
            break

    print('Five number solutions:')
    for (x, y) in get_solutions(generate_five_number_candidates(input_numbers), target):
        expr = parse(y, False)
        print(f"{expr} = {x}")
        index5 += 1
        if index5 == 4:
            break

    print('Six number solutions:')
    for (x, y) in get_solutions(generate_six_number_candidates(input_numbers), target):
        expr = parse(y, False)
        print(f"{expr} = {x}")
        index6 += 1
        if index6 == 4:
            break

