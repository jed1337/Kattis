n = int(input())
for _ in range(n):
    data = list(map(int, input().split()))
    can_power_on = data[0] - 1
    power_strip_outlets = sum(data[1:])

    print(power_strip_outlets-can_power_on)

