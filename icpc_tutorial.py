import math


def solve(m, n):
    if m >= n:
        print("AC")
    else:
        print("TLE")


m, n, t = list(map(int, input().split()))

factorials = [math.factorial(i) for i in range(13)]
power_of_2 = [2 ** i for i in range(30)]

if t == 1:
    if n > len(factorials):
        print("TLE")
    else:
        solve(m, factorials[n])
elif t == 2:
    if n > len(power_of_2):
        print("TLE")
    else:
        solve(m, power_of_2[n])
elif t == 3:
    solve(m, n ** 4)
elif t == 4:
    solve(m, n ** 3)
elif t == 5:
    solve(m, n ** 2)
elif t == 6:
    solve(m, n * math.log(n, 2))
elif t == 7:
    solve(m, n)
