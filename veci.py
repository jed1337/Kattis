from itertools import permutations


def get_result(x, valid_data):
    for i in range(len(valid_data)):
        if valid_data[i] == int(x):
            if i + 1 == len(valid_data):
                return 0
            else:
                return valid_data[i + 1]


x = input()

tuple_to_int = lambda y: int(''.join(y))
keep_valid_data = lambda y: len(str(y)) == len(x)

x_permutations = set(map(tuple_to_int, permutations(x)))

valid_data = set(filter(keep_valid_data, x_permutations))
valid_data = sorted(list(valid_data))

print(get_result(x, valid_data))
