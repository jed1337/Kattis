from collections import defaultdict

try:
    babelfish = defaultdict(lambda: "eh")

    is_input_mode = True
    while True:
        line = input()
        if line=="":
            is_input_mode = False
            continue

        if is_input_mode:
            english, pig_latin = line.split()
            babelfish[pig_latin] = english
        else:
            print(babelfish[line])
except EOFError:
    pass
