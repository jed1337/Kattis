test_cases = int(input())
for _ in range(test_cases):
    r, e, c = list(map(int, input().split()))

    if e-c > r:
        print("advertise")
    elif r > e - c:
        print("do not advertise")
    else:
        print("does not matter")
