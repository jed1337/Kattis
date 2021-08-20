from functools import cmp_to_key


def get_groups():
    groups, group = [], []
    try:
        while True:
            word = input()
            if word == '':
                groups.append(group)
                group = []
            else:
                group.append(word)
    except EOFError:
        pass

    groups.append(group)

    return groups


def cmp_items(a, b):
    if a[::-1] > b[::-1]:
        return 1
    else:
        return -1


groups = get_groups()
for i in range(len(groups)):
    group = groups[i]

    max_length = max(list(map(len, group)))
    group.sort(key=cmp_to_key(cmp_items))

    for word in group:
        print(word.rjust(max_length))

    if i < len(groups) - 1:
        print()
