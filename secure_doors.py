building = set()

for _ in range(int(input())):
    op_code, name = input().split()
    output = ""
    if op_code == "entry":
        if name in building:
            output = "{} entered (ANOMALY)"
        else:
            output = "{} entered"
        building.add(name)
    else:
        if name in building:
            output = "{} exited"
        else:
            output = "{} exited (ANOMALY)"
        if name in building:
            building.remove(name)

    print(output.format(name))
