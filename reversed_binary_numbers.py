n = int(input())
n = bin(n)
n = n[2:]  # remove the 0b part
n = n[::-1]  # reverse
print(int(n, 2))
