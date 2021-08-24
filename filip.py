a, b = list(map(lambda x: int(x[::-1]), input().split()))
if a > b:
    print(a)
else:
    print(b)
