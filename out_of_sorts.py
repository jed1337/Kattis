def binary_search(arr, x):
    lo = 0
    hi = len(arr) - 1

    while hi >= lo:
        mid = lo + (hi - lo) // 2
        if x == arr[mid]:
            return mid
        elif x < arr[mid]:
            hi = mid - 1
        else:
            lo = mid + 1

    return lo


n, m, a, c, x0 = list(map(int, input().split()))
count = 0

arr = []
for i in range(n):
    x0 = (a * x0 + c) % m
    arr.append(x0)

for i in range(len(arr)):
    if binary_search(arr, arr[i]) == i:
        count += 1

print(count)
