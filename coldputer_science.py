input()
temperatures = list(map(int, input().split()))
below_zero_count = len(list(filter(lambda x: x<0, temperatures)))
print(below_zero_count)