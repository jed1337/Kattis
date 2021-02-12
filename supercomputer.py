def flip(array, flip_bit):
    if array[flip_bit] == 0:
        array[flip_bit] = 1
    else:
        array[flip_bit] = 0


n, k = list(map(int, input().split()))
array = [0] * (n + 1)

for _ in range(k):
    line = input()
    if line[0] == 'F':
        _, flip_bit = line.split()
        flip_bit = int(flip_bit)
        flip(array, flip_bit)
    else:
        _, l, r = line.split()
        l = int(l)
        r = int(r)
        bounded_array = array[l:r + 1]
        print(len(list(filter(lambda x: x == 1, bounded_array))))
