word = input()
shortest = word
for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        first = word[0:i]
        second = word[i:j]
        third = word[j:len(word)]

        combined = first[::-1] + second[::-1] + third[::-1]
        shortest = min(combined, shortest)

print(shortest)
