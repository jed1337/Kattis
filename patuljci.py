limit = 9


def get_invalid():
    for i in range(limit):
        for j in range(i + 1, limit):
            if total - dwarves[i] - dwarves[j] == 100:
                return i, j


dwarves = [int(input()) for _ in range(limit)]
total = sum(dwarves)

invalid = get_invalid()
for i in range(limit):
    if i in invalid:
        continue
    print(dwarves[i])
