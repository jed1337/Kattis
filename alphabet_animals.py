from collections import defaultdict


def solve(choices, letter_dict, starting_letter):
    for choice in choices:
        if choice[-1] == starting_letter and letter_dict[choice[-1]] == 1:
            return choice + "!"
        elif letter_dict[choice[-1]] == 0:
            return choice + "!"

    if choices:
        return choices[0]
    else:
        return "?"


starting_letter = input()[-1]
animal_count = int(input())

letter_dict = defaultdict(lambda: 0)

animals = []
for _ in range(animal_count):
    animal = input()

    letter_dict[animal[0]] += 1
    animals.append(animal)

choices = list(filter(lambda x: x[0] == starting_letter, animals))

print(solve(choices, letter_dict, starting_letter))
