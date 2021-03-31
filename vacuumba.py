import math

for _ in range(int(input())):
    current_angle = 90
    pos_x = 0.0
    pos_y = 0.0

    m = int(input())
    for _ in range(m):
        angle, distance = list(map(float, input().split()))
        current_angle += angle

        pos_x += distance * math.cos(math.radians(current_angle))
        pos_y += distance * math.sin(math.radians(current_angle))

    print(pos_x, pos_y)