def coord(lines, coord):
    row, column = coord
    return lines[row][column]


def has_building():
    return coord(lines, north_west) == "#" or \
           coord(lines, north_east) == "#" or \
           coord(lines, south_west) == "#" or \
           coord(lines, south_east) == "#"


def get_squash_count():
    squash_count = 0
    if coord(lines, north_west) == "X":
        squash_count += 1
    if coord(lines, north_east) == "X":
        squash_count += 1
    if coord(lines, south_west) == "X":
        squash_count += 1
    if coord(lines, south_east) == "X":
        squash_count += 1

    return squash_count


r, c = list(map(int, input().split()))
lines = [input() for _ in range(r)]

squash_arr = [0, 0, 0, 0, 0]
for i in range(r - 1):
    for j in range(c - 1):
        north_west = (i, j)
        north_east = (i, j + 1)
        south_west = (i + 1, j)
        south_east = (i + 1, j + 1)

        if has_building():
            continue

        squash_arr[get_squash_count()] += 1

for i in range(5):
    print(squash_arr[i])
