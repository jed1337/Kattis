n=int(input())
prices = list(map(int, input().rstrip().split()))
prices.sort(reverse=True)

print(sum(prices[2::3]))