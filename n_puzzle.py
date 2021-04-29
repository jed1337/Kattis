def manhattan_distance(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])


puzzle_dict = {
    'A': (0, 0),
    'B': (0, 1),
    'C': (0, 2),
    'D': (0, 3),
    'E': (1, 0),
    'F': (1, 1),
    'G': (1, 2),
    'H': (1, 3),
    'I': (2, 0),
    'J': (2, 1),
    'K': (2, 2),
    'L': (2, 3),
    'M': (3, 0),
    'N': (3, 1),
    'O': (3, 2)
}

size = 4
puzzle = [input() for _ in range(size)]

total_distance = 0
for i in range(size):
    for j in range(size):
        coord = (i, j)
        letter = puzzle[i][j]

        if letter == '.':
            continue

        total_distance += manhattan_distance(coord, puzzle_dict[letter])

print(total_distance)
