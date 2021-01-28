actual = list(map(int, input().split()))
expected = [1, 1, 2, 2, 2, 8]

result = []
for i in range(len(actual)):
    result.append(expected[i] - actual[i])

print(" ".join(map(str, result)))