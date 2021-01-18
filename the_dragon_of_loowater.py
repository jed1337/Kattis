while True:
    n, m = list(map(int, input().rstrip().split()))
    head_diameters = sorted([int(input()) for _ in range(n)])
    knight_heights = sorted([int(input()) for _ in range(m)])

    if n == 0 and m == 0:
        break

    cost = 0
    is_doomed = False
    knight_index = 0

    for diameter in head_diameters:
        while knight_index < len(knight_heights) and diameter > knight_heights[knight_index]:
            knight_index += 1

        if knight_index >= len(knight_heights):
            is_doomed = True
            break

        height_value = knight_heights[knight_index]
        cost += height_value

        knight_index += 1

    if not is_doomed:
        print(cost)
    else:
        print("Loowater is doomed!")
