while True:
    list_size = int(input())
    if list_size == 0:
        break

    orig_list1 = [int(input()) for _ in range(list_size)]
    orig_list2 = [int(input()) for _ in range(list_size)]

    sorted_list_1 = sorted(orig_list1)
    sorted_list_2 = sorted(orig_list2)

    correspondence = {}
    for i in range(list_size):
        correspondence[sorted_list_1[i]] = sorted_list_2[i]

    for orig_elem in orig_list1:
        print(correspondence[orig_elem])

    print()