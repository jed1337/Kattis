equivalence = {
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: 'a',
    11: 'b',
    12: 'c',
    13: 'd',
    14: 'e',
    15: 'f',
    16: 'g',
    17: 'h',
    18: 'i',
    19: 'j',
    20: 'k',
    21: 'l',
    22: 'm',
    23: 'n',
    24: 'o',
    25: 'p',
    26: 'q',
    27: 'r',
    28: 's',
    29: 't',
    30: 'u',
    31: 'v',
    32: 'w',
    33: 'x',
    34: 'y',
    35: 'z',
    36: '0'
}


def is_base_1(x, op, y, z):
    if all_ones(x) and all_ones(y) and all_ones(z):
        x = len(x)
        y = len(y)
        z = len(z)

        x_op_y = eval("{}{}{}".format(x, op, y))
        return x_op_y == z

    return False


def all_ones(string):
    return all(map(lambda x: x == "1", string))


def is_other_base(x, op, y, z):
    try:
        x = int(x, base)
        y = int(y, base)
        z = int(z, base)

        x_op_y = eval("{}{}{}".format(x, op, y))
        return x_op_y == z
    except ValueError:
        return False


for _ in range(int(input())):
    x, op, y, _, z = input().split()

    results = ""
    if is_base_1(x, op, y, z):
        results += "1"

    for base in range(2, 37):
        if is_other_base(x, op, y, z):
            results += equivalence[base]

    if results:
        print(results)
    else:
        print("invalid")
