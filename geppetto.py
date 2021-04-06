from collections import defaultdict


def solve(current, invalid_combinations, chosen):
    if current == 0:
        return 1

    total_ways = 0

    current_is_valid = True
    for value in invalid_combinations[current]:
        if value in chosen:
            current_is_valid = False

    # exclude current item
    total_ways += solve(current - 1, invalid_combinations, chosen)

    # include current item
    if current_is_valid:
        total_ways += solve(current - 1, invalid_combinations, chosen + [current])

    return total_ways


n, m = list(map(int, input().split()))

invalid_combinations = defaultdict(lambda: set())
for _ in range(m):
    a, b = sorted(list(map(int, input().split())))
    invalid_combinations[a].add(b)

total_ways = solve(n, invalid_combinations, [])
print(total_ways)
