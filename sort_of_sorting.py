from functools import cmp_to_key


def cmp_items(a, b):
    if a[0] > b[0]:
        return 1
    elif a[0] < b[0]:
        return -1

    if a[1] > b[1]:
        return 1
    elif a[1] < b[1]:
        return -1

    return 0


while True:
    n = int(input())
    if n == 0:
        break
    names = [input() for _ in range(n)]
    names.sort(key=cmp_to_key(cmp_items))
    for name in names:
        print(name)
    print()