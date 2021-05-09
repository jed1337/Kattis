data = [int(input()) for _ in range(10)]

modded = map(lambda x: x % 42, data)
unique = set(modded)
print(len(unique))
