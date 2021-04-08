ops = ["*", "+", "-", "//"]


def get_result(expected):
    for o1 in ops:
        for o2 in ops:
            for o3 in ops:
                try:
                    if eval("4 {} 4 {} 4 {} 4".format(o1, o2, o3)) == expected:
                        return list(map(replace_floor_div_with_div, (o1, o2, o3)))
                except ZeroDivisionError:
                    continue
    return None


def replace_floor_div_with_div(x):
    return "/" if x == "//" else x


m = int(input())
for _ in range(m):
    expected = int(input())

    result = get_result(expected)
    if result:
        print("4 {} 4 {} 4 {} 4 = {}"
              .format(result[0], result[1], result[2], expected))
    else:
        print("no solution")
