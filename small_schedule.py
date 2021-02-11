def solve(q, m, s, l):
    time = 0

    # spread out the l tasks amongst m
    if l >= m:
        time += (l // m) * q
        l %= m

    # If there are no more l tasks, spread out the s tasks amongst m
    if l == 0:
        time += (s // m)
        return time + (0 if s % m == 0 else 1)

    # Allocate the remaining l tasks in m
    time += q

    # Allocate what s tasks we can in the remaining machines to even everything off
    s -= (m - l) * q

    if s <= 0:
        return time

    # Spread out the last s tasks amongst m
    time += s // m
    return time + (0 if s % m == 0 else 1)


q, m, s, l = list(map(int, input().split()))

print(solve(q, m, s, l))
