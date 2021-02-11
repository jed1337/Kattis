def digit_sum(i):
    return sum(map(int, str(i)))


l = int(input())
d = int(input())
x = int(input())

n = 0
m = 0
for i in range(l, d + 1):
    if digit_sum(i) == x:
        n = i
        break

for i in range(d, l - 1, -1):
    if digit_sum(i) == x:
        m = i
        break

print(n)
print(m)
