def is_ruler(marks):
    combinations = []
    for i in range(len(marks)):
        for j in range(i + 1, len(marks)):
            if i < 0 or j < 0:
                return False
            difference = marks[j] - marks[i]
            if difference in combinations:
                return False
            else:
                combinations.append(difference)
    return True


def get_combinations(marks):
    combinations = []
    for i in range(len(marks)):
        for j in range(i + 1, len(marks)):
            difference = marks[j] - marks[i]
            combinations.append(difference)
    return sorted(combinations)


try:
    while True:
        marks = sorted(list(map(int, input().split())))
        if not is_ruler(marks):
            print("not a ruler")
            continue

        combinations = get_combinations(marks)
        greatest_mark = marks[-1]
        missing = []
        for i in range(1, greatest_mark):
            if i not in combinations:
                missing.append(i)
        if missing:
            print("missing {}".format(" ".join(map(str, missing))))
        else:
            print("perfect")
except EOFError:
    pass
