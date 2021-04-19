import math


def get_a(d, s):
    hi, lo = 10000000000, 1e-10
    threshold = 1e-10
    while hi - lo > threshold:
        mid = lo + (hi - lo) / 2

        if mid + s < mid * math.cosh(d / (2 * mid)):
            lo = mid
        else:
            hi = mid
    return lo


def length(a, d):
    return 2 * a * math.sinh(d / (2 * a))


d, s = map(int, input().split())

mid = get_a(d, s)
print(length(mid, d))
