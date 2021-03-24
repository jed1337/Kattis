memo_limit = int(1e6 + 1)
inf = int(1e5)


def simplify(value):
    while value % 10 == 0:
        value /= 10
    return value % inf


def get_first_non_zero(value):
    while value % 10 == 0:
        value /= 10

    return value % 10


memo = [0] * memo_limit
memo[0] = 1
memo[1] = 1

ans = 1
for i in range(2, memo_limit):
    ans *= i
    ans = simplify(ans)
    memo[i] = get_first_non_zero(ans)

while True:
    query = int(input())
    if query == 0:
        break
    print(int(memo[query]))
