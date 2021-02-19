def swap(arr, i1, i2):
    arr[i1], arr[i2] = arr[i2], arr[i1]


arr = [0, 1, 0, 0]

string = input()
for char in string:
    if char == 'A':
        swap(arr, 1, 2)
    elif char == 'B':
        swap(arr, 2, 3)
    else:
        swap(arr, 1, 3)

if arr[1] == 1:
    print(1)
elif arr[2] == 1:
    print(2)
else:
    print(3)
