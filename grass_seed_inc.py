seed_cost = float(input())
count = int(input())

total_lawn_area = 0.0
for i in range(count):
    width, length = list(map(float, input().split()))
    total_lawn_area += width * length

print(seed_cost * total_lawn_area)