import math
input()  # We don't need to use n, m, k

plot_radiuses = list(map(int, input().rstrip().split()))
circle_house_diameters = list(map(lambda x: int(x) * 2, input().rstrip().split()))
square_house_diagonal_lengths = list(map(lambda x: math.sqrt(2* (int(x)**2)), input().rstrip().split()))

plot_diameters = sorted(list(map(lambda x: x * 2, plot_radiuses)))
house_lengths = sorted(circle_house_diameters + square_house_diagonal_lengths)

fit_count = 0

p_index = 0
h_index = 0
while p_index < len(plot_diameters) and h_index < len(house_lengths):
    plot = plot_diameters[p_index]
    house = house_lengths[h_index]

    if plot > house:
        fit_count += 1
        p_index += 1
        h_index += 1
    elif plot <= house:
        p_index += 1

print(fit_count)
