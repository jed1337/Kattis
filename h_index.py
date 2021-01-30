n = int(input())
citations = [int(input()) for _ in range(n)]
citations.sort(reverse=True)

h_index = 0
for i in range(n):
    if citations[i] >= i + 1:
        h_index += 1
    else:
        break

print(h_index)