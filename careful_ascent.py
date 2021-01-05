mal_x, mal_y = list(map(int, input().split()))
n = int(input())
shields = []
for i in range(n):
    lower_bound, upper_bound, factor = input().split()
    shields.append([int(lower_bound), int(upper_bound), float(factor)])

shields.sort(key=lambda shield: shield[0])
shields.append([mal_y])
speed = shields[0][0]

for i in range(n):
    lower_bound, upper_bound, factor = shields[i]
    next_lower_bound = shields[i+1][0]

    speed += (upper_bound - lower_bound) * factor
    speed += next_lower_bound - upper_bound

print(mal_x/speed)