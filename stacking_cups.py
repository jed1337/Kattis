lines = [input().split() for _ in range(int(input()))]

cups = []
for line in lines:
    a, b = line
    if a.isdigit():
        a = int(a)
        cups.append((a/2, b))
    else:
        b = int(b)
        cups.append((b, a))

cups.sort()
for cup in cups:
    print(cup[1])
