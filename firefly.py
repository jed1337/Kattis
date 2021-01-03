import sys

n, h = list(map(int, input().split()))
# n = 14
# h = 5

bottom = [0 for i in range(h)]
top = [0 for i in range(h)]

# array = [1, 3, 4, 2, 2, 4, 3, 4, 3, 3, 3, 2, 3, 3]
for i in range(n):
    # height = array[i]
    height = int(input())
    if i % 2 == 0:
        bottom[height - 1] += 1
    else:
        top[h - height] += 1

cumulativeSumBottom = 0
for i in reversed(range(h)):
    cumulativeSumBottom += bottom[i]
    bottom[i] = cumulativeSumBottom

cumulativeSumTop = 0
for i in range(h):
    cumulativeSumTop += top[i]
    top[i] = cumulativeSumTop

min_obstacles_to_hit = sys.maxsize
count = 0
for i in range(h):
    if bottom[i] + top[i] < min_obstacles_to_hit:
        min_obstacles_to_hit = bottom[i] + top[i]
        count = 1
    elif bottom[i] + top[i] == min_obstacles_to_hit:
        count += 1

print(min_obstacles_to_hit, count)
