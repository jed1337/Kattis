def least_common(arr):
    return min(arr, key=arr.count)


xs = []
ys = []
for i in range(3):
    x, y = list(map(int, input().split()))
    xs.append(x)
    ys.append(y)

print(least_common(xs), least_common(ys))
