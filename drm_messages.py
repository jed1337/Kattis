from string import ascii_uppercase

alphabet = ascii_uppercase
alphabet_dict = {letter: value for (value, letter) in enumerate(ascii_uppercase)}


def get_sum(string):
    return sum(map(lambda x: alphabet_dict[x], string))


def rotate(string, sum):
    result = ""
    for letter in string:
        result += alphabet[(alphabet_dict[letter] + sum) % len(alphabet)]

    return result


encrypted = input()

first_half = encrypted[0:len(encrypted) // 2]
second_half = encrypted[len(encrypted) // 2:]

first_sum = get_sum(first_half)
second_sum = get_sum(second_half)

first_rotation = rotate(first_half, first_sum)
second_rotation = rotate(second_half, second_sum)

result = ""
for i in range(len(first_rotation)):
    result += rotate(first_rotation[i], get_sum(second_rotation[i]))

print(result)
