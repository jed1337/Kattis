a, b, c = sorted(list(map(int, input().split())))
sorting = input()

result = []
for order in sorting:
    if order == 'A':
        result.append(a)
    elif order == 'B':
        result.append(b)
    else:
        result.append(c)

print(" ".join(map(str, result)))
