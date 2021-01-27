def solve(row1, row2, all_weights):
    if is_paired(row1) and is_paired(row2):
        return 0

    lo = 0
    hi = len(all_weights)

    #O(log N)
    while lo < hi:
        mid = lo + (hi - lo) // 2

        #O(N)
        filtered_row1 = keep_heavier_than(row1, all_weights[mid])
        filtered_row2 = keep_heavier_than(row2, all_weights[mid])

        #O(N)
        if is_paired(filtered_row1) and is_paired(filtered_row2):
            hi = mid
        else:
            lo = mid + 1

    return all_weights[lo]


def is_paired(row):
    if len(row) % 2 == 1:
        return False

    for i in range(0, len(row), 2):
        if row[i] != row[i + 1]:
            return False

    return True


def keep_heavier_than(row, threshold):
    return list(filter(lambda x: x > threshold, row))


# input()
# row1 = list(map(int, input().split()))
# row2 = list(map(int, input().split()))

row1=[7,7,15,4,4,5,5,3,3,9,9,1,1]
row2=[2,2, 15]


all_weights = sorted(list(set(row1 + row2)))

print(solve(row1, row2, all_weights))
