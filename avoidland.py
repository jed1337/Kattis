n = int(input())
rows = []
columns = []
for _ in range(n):
    row, column = list(map(int, input().split()))
    rows.append(row)
    columns.append(column)

rows.sort()
columns.sort()

moves = 0
for i in range(n):
    diagonal = i+1
    moves += abs(rows[i] - diagonal)
    moves += abs(columns[i] - diagonal)

print(moves)