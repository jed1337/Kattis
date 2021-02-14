from sys import stdin

for line in stdin:
    if line == '':
        break
    val1, val2 = list(map(int, line.split()))
    print(abs(val1-val2))

# while True:
#     line = input()
#     if line == '':
#         break
#     val1, val2 = list(map(int, line.split()))
#     print(abs(val1-val2))