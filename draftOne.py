import itertools

TargetNumber = int(input("Enter Target Number: "))

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))
num4 = int(input("Enter Fourth Number: "))
num5 = int(input("Enter Fifth Number: "))
num6 = int(input("Enter Sixth Number: "))

NumberList = [num1, num2, num3, num4, num6, num6]

print(NumberList)

single_digit_solutions = []
# two_digit_strings = set()
# two_digit_integer_outputs_and_strings = {}
# three_digit_strings = set()
# three_digit_integer_outputs_and_strings = {}


def Single_number_solutions(any_list):
    for i in any_list:
        if i == TargetNumber:
            single_digit_solutions.append(i)
    return single_digit_solutions


#def Two_number_solutions(a, b):
#     if a * b == TargetNumber:
#         two_digit_strings.add(str(a) + '*' + str(b))
#     if a + b == TargetNumber:
#         two_digit_strings.add(str(a) + '+' + str(b))
#     if a - b == TargetNumber:
#         two_digit_strings.add(str(a) + '-' + str(b))
#     if b - a == TargetNumber:
#         two_digit_strings.add(str(b) + '-' + str(a))
#     if a / b == TargetNumber:
#         two_digit_strings.add(str(a) + '/' + str(b))
#     if b / a == TargetNumber:
#         two_digit_strings.add(str(b) + '-' + str(a))
#
#     return two_digit_strings
#
#
# def Three_number_solutions(a, b, c):
#
#     for key in Two_number_integers(a, b):
#         if key * c == TargetNumber:
#             three_digit_strings.add('(' + two_digit_integer_outputs_and_strings.get(key) + ')' + '*' + str(c))
#     for key in Two_number_integers(a, b):
#         if key + c == TargetNumber:
#             three_digit_strings.add('(' + two_digit_integer_outputs_and_strings.get(key) + ')' + '+' + str(c))
#     for key in Two_number_integers(a, b):
#         if key - c == TargetNumber:
#             three_digit_strings.add('(' + two_digit_integer_outputs_and_strings.get(key) + ')' + '-' + str(c))
#     for key in Two_number_integers(a, b):
#         if c - key == TargetNumber:
#             three_digit_strings.add(str(c) + '-' + '(' + two_digit_integer_outputs_and_strings.get(key) + ')')
#     for key in Two_number_integers(a, b):
#         if key / c == TargetNumber:
#             three_digit_strings.add('(' + two_digit_integer_outputs_and_strings.get(key) + ')' + '/' + str(c))
#     for key in Two_number_integers(a, b):
#         if c / key == TargetNumber:
#             three_digit_strings.add(str(c) + '/' + '(' + two_digit_integer_outputs_and_strings.get(key) + ')')
#
#     """
#     (a, c)
#     """
#
#     for key in Two_number_integers(a, c):
#         if key * b == TargetNumber:
#             three_digit_strings.add('(' + two_digit_integer_outputs_and_strings.get(key) + ')' + '*' + str(b))
#     for key in Two_number_integers(a, c):
#         if key + b == TargetNumber:
#             three_digit_strings.add('(' + two_digit_integer_outputs_and_strings.get(key) + ')' + '+' + str(b))
#     for key in Two_number_integers(a, c):
#         if key - b == TargetNumber:
#             three_digit_strings.add('(' + two_digit_integer_outputs_and_strings.get(key) + ')' + '-' + str(b))
#     for key in Two_number_integers(a, c):
#         if b - key == TargetNumber:
#             three_digit_strings.add(str(b) + '-' + '(' + two_digit_integer_outputs_and_strings.get(key) + ')')
#     for key in Two_number_integers(a, c):
#         if key / b == TargetNumber:
#             three_digit_strings.add('(' + two_digit_integer_outputs_and_strings.get(key) + ')' + '/' + str(b))
#     for key in Two_number_integers(a, c):
#         if b / key == TargetNumber:
#             three_digit_strings.add(str(b) + '/' + '(' + two_digit_integer_outputs_and_strings.get(key) + ')')
#     return three_digit_strings
#
#     """
#     (b, c)
#     """
#
#     for key in Two_number_integers(b, c):
#         if key * a == TargetNumber:
#             three_digit_strings.add('(' + two_digit_integer_outputs_and_strings.get(key) + ')' + '*' + str(a))
#     for key in Two_number_integers(b, c):
#         if key + a == TargetNumber:
#             three_digit_strings.add('(' + two_digit_integer_outputs_and_strings.get(key) + ')' + '+' + str(a))
#     for key in Two_number_integers(b, c):
#         if key - a == TargetNumber:
#             three_digit_strings.add('(' + two_digit_integer_outputs_and_strings.get(key) + ')' + '-' + str(a))
#     for key in Two_number_integers(b, c):
#         if a - key == TargetNumber:
#             three_digit_strings.add(str(a) + '-' + '(' + two_digit_integer_outputs_and_strings.get(key) + ')')
#     for key in Two_number_integers(b, c):
#         if key / a == TargetNumber:
#             three_digit_strings.add('(' + two_digit_integer_outputs_and_strings.get(key) + ')' + '/' + str(a))
#     for key in Two_number_integers(b, c):
#         if a / key == TargetNumber:
#             three_digit_strings.add(str(a) + '/' + '(' + two_digit_integer_outputs_and_strings.get(key) + ')')
#     return three_digit_strings
#
#
# def Two_number_integers(a, b):
#     if isinstance(a * b, int):
#         two_digit_integer_outputs_and_strings[a * b] = (str(a) + '*' + str(b))
#     if isinstance((a + b), int):
#         two_digit_integer_outputs_and_strings[a + b] = (str(a) + '+' + str(b))
#     if isinstance((a - b), int):
#         two_digit_integer_outputs_and_strings[a - b] = (str(a) + '-' + str(b))
#     if isinstance((b - a), int):
#         two_digit_integer_outputs_and_strings[b - a] = (str(b) + '-' + str(a))
#     if isinstance((a / b), int):
#         two_digit_integer_outputs_and_strings[b / a] = (str(b) + '/' + str(a))
#     if isinstance((b / a), int):
#         two_digit_integer_outputs_and_strings[a / b] = (str(a) + '/' + str(b))
#
#     return two_digit_integer_outputs_and_strings
#
#
#
#
target_ones = Single_number_solutions(NumberList)
#
# target_twos = Two_number_solutions(num1, num2) | Two_number_solutions(num1, num3) | Two_number_solutions(num2, num3)
#
#
#
# target_threes = Three_number_solutions(num1, num2, num3)
# integer_twos = Two_number_integers(num1, num2) | Two_number_integers(num1, num3) | Two_number_integers(num2, num3)

print(f'One number solutions: {target_ones}')

print(f'Two number solutions: {target_twos}')

print(f'Three number solutions: {target_threes}')

print(f'Two number integer output list: {integer_twos}')

print(f'Three number integer output list: ')