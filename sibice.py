n, w, h = list(map(int, input().split()))
for _ in range(n):
    c = int(input())
    if c**2 <= w**2 + h**2:
        print("DA")
    else:
        print("NE")
