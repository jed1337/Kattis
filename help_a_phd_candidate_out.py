for i in range(int(input())):
    line = input()
    if line == "P=NP":
        print("skipped")
    else:
        a, b = list(map(int, line.split("+")))
        print(a + b)
