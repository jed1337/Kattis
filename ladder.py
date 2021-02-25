from math import ceil, sin, radians

h, v = list(map(int, input().split()))

print(ceil(h/sin(radians(v))))