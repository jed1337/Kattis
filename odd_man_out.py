n = int(input())
for i in range(n):
    input()
    guests = list(map(int, input().rstrip().split()))
    odd_man_out = min(guests, key=guests.count)
    print("Case #{}: {}".format((i+1), odd_man_out))