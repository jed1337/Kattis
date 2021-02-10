import math

# q, m, s, l = list(map(int, input().split()))

# q, m, s, l = 2, 4, 3, 6
# q, m, s, l = 3, 4, 3, 5
# q, m, s, l = 10, 2, 0, 1
# q, m, s, l = 5, 2, 8, 3
q, m, s, l = 2, 1000000, 500000, 500000

time = 0

# Spread out l amongst all the machines
time += (l // m) * q
time += (math.ceil((l % m) / m)) * q

# Allocate the areas not given a slot to s
not_given_a_slot = m - (l % m)
s -= not_given_a_slot * q

if s <= 0:
    s = 0

# Spread out s amongst all the machines
time += (s // m)
time += math.ceil((s % m) / m)

print(time)
