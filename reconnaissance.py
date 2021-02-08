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


vehicle_count = int(input())
vehicles = []
for _ in range(vehicle_count):
    position, velocity = list(map(int, input().split()))
    vehicles.append([position, velocity])

lo = 0
hi = 1000000
while lo < hi:
    mid1 = lo + (hi - lo) // 3
    mid2 = mid1 + lo + (hi - lo) // 3

    separation1 = separation(mid1, vehicles)
    separation2 = separation(mid2, vehicles)
    separationHi = separation(hi, vehicles)

    if separation1 < separation2:
        hi = mid1
    elif separation2 < separationHi:
        lo = mid1
        hi = mid2
    else:
        lo = mid2

print(separation(hi, vehicles))
