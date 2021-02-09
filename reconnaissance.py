import math

POSITION_INDEX = 0
VELOCITY_INDEX = 1


def separation(time, vehicles):
    left_most = math.inf
    right_most = -math.inf

    for vehicle in vehicles:
        vehicle_position = vehicle[POSITION_INDEX] + (vehicle[VELOCITY_INDEX] * time)
        left_most = min(left_most, vehicle_position)
        right_most = max(right_most, vehicle_position)

    return right_most - left_most


def binary_search(vehicles):
    lo = 0
    hi = 1000000
    threshold = 1e-4

    iteration_limit = 50
    iterations = 0

    while abs(hi - lo) > threshold and iterations < iteration_limit:
        mid = lo + (hi - lo) / 2
        mid_left = mid - threshold
        mid_right = mid + threshold

        separation_mid = separation(mid, vehicles)
        separation_left = separation(mid_left, vehicles)
        separation_right = separation(mid_right, vehicles)

        if separation_left < separation_mid and separation_left < separation_right:
            hi = mid_left
        elif separation_mid < separation_left and separation_mid < separation_right:
            lo = mid_left
            hi = mid_right
        else:
            lo = mid_right

        iterations += 1

    return hi


vehicle_count = int(input())
vehicles = []

for _ in range(vehicle_count):
    position, velocity = list(map(int, input().split()))
    vehicles.append([position, velocity])

time = binary_search(vehicles)
print(separation(time, vehicles))
