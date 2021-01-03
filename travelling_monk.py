def get_total_height(climb_list):
    return sum([climb_item[0] for climb_item in climb_list])


def get_total_time(climb_list):
    return sum([climb_item[1] for climb_item in climb_list])


def get_height_at_time(climb_list, is_ascending, time):
    total_height_climbed = 0
    partial_height_climbed = 0

    for climb_item in climb_list:
        if climb_item[1] - time < 0:
            total_height_climbed += climb_item[0]
            time -= climb_item[1]
        else:
            partial_height_climbed = time * (climb_item[0] / climb_item[1])
            break

    if is_ascending:
        return total_height_climbed + partial_height_climbed
    else:
        return abs(get_total_height(climb_list) - total_height_climbed - partial_height_climbed)


a, d = list(map(int, input().split()))
ascent_list = []
descent_list = []

# ascent_list = [[2, 3], [0, 5], [3, 1]]
# descent_list = [[3, 4], [0, 2], [2, 2]]

for i in range(a):
    ascent_height, time = list(map(int, input().split()))
    ascent_list.append([ascent_height, time])

for i in range(d):
    descent_height, time = list(map(int, input().split()))
    descent_list.append([descent_height, time])

lo = 0
hi = max(get_total_time(ascent_list), get_total_time(descent_list))
threshold = 1e-6

while abs(hi - lo) > threshold:
    middle_time = lo + (hi - lo) / 2
    ascent_height = get_height_at_time(ascent_list, True, middle_time)
    descent_height = get_height_at_time(descent_list, False, middle_time)

    if ascent_height < descent_height:
        lo = middle_time
    else:
        hi = middle_time

print('%.6f' % lo)
