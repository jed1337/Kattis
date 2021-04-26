SOURNESS_INDEX = 0
BITTERNESS_INDEX = 1


def decimal_to_binary_array(i, length_limit):
    binary = bin(i).replace("0b", "").zfill(length_limit)
    binary_array = list(map(lambda x: True if x == "1" else False, binary))

    return binary_array


def get_difference(ingredients, combination):
    sourness_product = 1
    bitterness_sum = 0
    for i in range(len(ingredients)):
        if combination[i]:
            sourness_product *= ingredients[i][SOURNESS_INDEX]
            bitterness_sum += ingredients[i][BITTERNESS_INDEX]

    return abs(sourness_product - bitterness_sum)


n = int(input())
ingredients = [list(map(int, input().split())) for _ in range(n)]

min_difference = 1e8
for i in range(1, 2 ** n):
    combination = decimal_to_binary_array(i, n)
    difference = get_difference(ingredients, combination)
    min_difference = min(difference, min_difference)

print(min_difference)
