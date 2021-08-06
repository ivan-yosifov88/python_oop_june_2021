from itertools import permutations


def possible_permutations(ll):
    for line in permutations(ll):
        yield list(line)

# def possible_permutations(ll_of_numbers, index=0):
#     if index + 1 >= len(ll_of_numbers):
#         yield ll_of_numbers
#     else:
#         for permutation in possible_permutations(ll_of_numbers, index + 1):
#             yield permutation
#
#         for i in range(index + 1, len(ll_of_numbers)):
#             ll_of_numbers[index], ll_of_numbers[i] = ll_of_numbers[i], ll_of_numbers[index]
#             for permutation in possible_permutations(ll_of_numbers, index+1):
#                 yield permutation
#             ll_of_numbers[index], ll_of_numbers[i] = ll_of_numbers[i], ll_of_numbers[index]




[print(n) for n in possible_permutations([1, 2, 3])]