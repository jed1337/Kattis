team_count, _, _ = list(map(int, input().split()))
damaged = list(map(lambda x: int(x)-1, input().split()))
reserved = list(map(lambda x: int(x)-1, input().split()))

works = [True] * team_count

for i in range(team_count):
    if i in damaged:
        works[i] = False

for i in range(team_count):
    if works[i]:
        continue

    if i in damaged:
        if i-1 in reserved:
            works[i] = True
            damaged.remove(i)
            reserved.remove(i-1)
        elif i in reserved:
            works[i] = True
            damaged.remove(i)
            reserved.remove(i)
        elif i+1 in reserved:
            works[i] = True
            damaged.remove(i)
            reserved.remove(i+1)

print(works.count(False))