from collections import Counter


def solve_t1():
    sorted_values = sorted(set(values))
    target_value = 7777
    n = len(sorted_values)
    for i in range(n):
        lo = 0
        hi = n

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if sorted_values[mid] + sorted_values[i] == target_value:
                return "Yes"
            elif sorted_values[mid] + sorted_values[i] < target_value:
                lo = mid + 1
            else:
                hi = mid

    return "No"


n, t = list(map(int, input().split()))
values = list(map(int, input().split()))

if t == 1:
    print(solve_t1())
elif t == 2:
    unique = set(values)
    if len(unique) == len(values):
        print("Unique")
    else:
        print("Contains duplicate")
elif t == 3:
    counter = Counter(values)
    occurrences_needed = n / 2
    most_common = counter.most_common(1)[0]
    value, occurrences = most_common
    if occurrences > occurrences_needed:
        print(value)
    else:
        print(-1)
elif t == 4:
    sorted_values = sorted(values)
    if n % 2 == 1:
        print(sorted_values[n // 2])
    else:
        print(sorted_values[n // 2 - 1], sorted_values[n // 2])
elif t == 5:
    new_values = sorted(filter(lambda x: 100 <= x <= 999, values))
    print(" ".join(map(str, new_values)))
