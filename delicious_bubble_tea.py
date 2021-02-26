from math import floor

tea_count = int(input())
tea_prices = list(map(int, input().split()))
int(input())
topping_prices = list(map(int, input().split()))

for i in range(tea_count):
    combination_prices = list(map(int, input().split()))
    combination_prices = combination_prices[1:]

    tea_prices[i] += min(combination_prices)

money = int(input())

cheapest = sorted(tea_prices)[0]
max_students = floor(money / cheapest) - 1

if max_students <= 0:
    print(0)
else:
    print(max_students)
