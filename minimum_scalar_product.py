test_cases = int(input())
for i in range(1, test_cases + 1):
    element_count = int(input())
    v1 = sorted(list(map(int, input().split())))
    v2 = sorted(list(map(int, input().split())), reverse=True)

    minimum_scalar = 0
    for j in range(len(v1)):
        minimum_scalar += v1[j] * v2[j]

    print("Case #{}: {}".format(i, minimum_scalar))
