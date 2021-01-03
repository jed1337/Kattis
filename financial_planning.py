def can_repay(debt, investments, days):
    total_net_profit = 0

    PROFIT = 0
    COST = 1

    for investment in investments:
        temp_net_profit = investment[PROFIT] * days - investment[COST]

        if temp_net_profit > 0:
            total_net_profit += temp_net_profit
        if total_net_profit >= debt:
            return True

    return False


n, m = list(map(int, input().split()))

investments = []

for i in range(n):
    profit, cost = list(map(int, input().split()))
    investments.append([profit, cost])

lo = 0
hi = int(2e9) + 1

while lo < hi:
    middle = lo + (hi - lo) // 2

    if can_repay(m, investments, middle):
        hi = middle
    else:
        lo = middle + 1

print(lo)
