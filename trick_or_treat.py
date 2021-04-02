import math


def f(destination_x, houses):
    destination_y = 0

    max_time = 0
    for house in houses:
        x, y = house
        distance = math.sqrt((x - destination_x) ** 2 + (y - destination_y) ** 2)
        max_time = max(max_time, distance)

    return max_time


while True:
    house_count = int(input())

    if house_count == 0:
        break

    houses = []
    for _ in range(house_count):
        x, y = list(map(float, input().split()))
        houses.append([x, y])

    iteration_limit = 80
    iterations = 0
    lo = -200000
    hi = 200000
    threshold = 1e-6
    while abs(hi - lo) > threshold:
        mid1 = lo + (hi - lo) * (1 / 3)
        mid2 = lo + (hi - lo) * (2 / 3)

        if f(mid1, houses) < f(mid2, houses):
            hi = mid2
        else:
            lo = mid1

        iterations += 1

    print("{:.12f} {:.12f}".format(hi, f(hi, houses)))
    input()
