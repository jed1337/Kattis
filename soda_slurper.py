e, f, cost = list(map(int, input().split()))
empty_bottles = e + f
sodas_drank = 0

while True:
    soda = empty_bottles // cost
    empty_bottles %= cost

    sodas_drank += soda
    empty_bottles += soda

    if empty_bottles < cost:
        break

print(sodas_drank)