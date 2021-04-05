n, p, q = list(map(int, input().split()))

total_points = p+q
if total_points%(n*2) < n:
    print('paul')
else:
    print('opponent')
