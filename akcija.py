prices = [int(input()) for _ in range(int(input()))]
prices.sort(reverse=True)
minimum_price = sum(prices[::3] + prices[1::3])
print(minimum_price)
