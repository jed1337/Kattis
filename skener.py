r, c, zr, zc = list(map(int, input().split()))

data = [input() for _ in range(r)]

enlarged_row = []
for row in data:
    enlarged_column = []
    for char in row:
        enlarged_column.append(char*zc)
    enlarged_row.append(''.join(enlarged_column))

for row in enlarged_row:
    for i in range(zr):
        print(row)
