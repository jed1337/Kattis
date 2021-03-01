for _ in range(int(input())):
    turtles = list(map(int, input().split()))[0:-1]

    imports = 0
    for j in range(1, len(turtles)):
        if turtles[j] > (turtles[j-1] * 2):
            imports += turtles[j] - (turtles[j-1] * 2)

    print(imports)