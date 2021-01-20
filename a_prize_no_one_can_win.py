def max_marks(items, euro_limit):
    if len(items) == 1:
        return 1

    for min_index in range(len(items) - 1):
        max_index = min_index + 1
        if items[min_index] + items[max_index] > euro_limit:
            return max_index

    return len(items)


_, euro_limit = list(map(int, input().rstrip().split()))
items = sorted(list(map(int, input().rstrip().split())))

print(max_marks(items, euro_limit))
