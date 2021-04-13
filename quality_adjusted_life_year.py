n = int(input())
quality = []
for _ in range(n):
    q, y = list(map(float, input().split()))
    quality.append(q*y)

print(sum(quality))
