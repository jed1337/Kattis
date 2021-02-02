l, d, n = list(map(int, input().split()))
birds = sorted([int(input()) for _ in range(n)])

additional_birds = 0
current_position = 6
if not birds:
    additional_birds += (l - 12) // d + 1
else:
    for bird in birds:
        while current_position + d <= bird:
            additional_birds += 1
            current_position += d
        current_position = bird + d
    while current_position <= (l - 6):
        additional_birds += 1
        current_position += d

print(additional_birds)
