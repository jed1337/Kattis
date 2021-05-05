def f(x, y, h):
    a = x - 2 * h
    b = y - 2 * h

    return a * b * h


test_cases = int(input())
for _ in range(test_cases):
    x, y = list(map(int, input().split()))

    threshold = 1e-7
    lo = threshold
    hi = max(x, y) / 2
    while abs(hi - lo) > threshold:
        mid1 = lo + (hi - lo) * (1 / 3)
        mid2 = lo + (hi - lo) * (2 / 3)

        if f(x, y, mid1) < f(x, y, mid2):
            lo = mid1
        else:
            hi = mid2

    print(f(x, y, hi))
