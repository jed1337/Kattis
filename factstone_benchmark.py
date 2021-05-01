from math import log


def year_to_bits(year):
    while year % 10 != 0:
        year -= 1

    year -= 1960
    year = int(year / 10)

    return 2 ** (2 + year)


factstone_cache = {}
factorial_cache = {}

year = 1960
upper_bound = 2160
while year <= upper_bound:
    i = year_to_bits(year)
    factstone_cache[i] = 0
    year += 10

bits = 0
for i in range(1, 300000):
    bits += log(i, 2)
    factorial_cache[i] = bits

for i in range(1, 300000 - 1):
    j = i + 1

    for key in factstone_cache.keys():
        if factstone_cache[key]:
            continue
        if factorial_cache[i] < key < factorial_cache[j]:
            factstone_cache[key] = i

while True:
    y = int(input())
    if y == 0:
        break
    print(factstone_cache[year_to_bits(y)])
