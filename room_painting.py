def lower_bound(array, search_key):
    lo = 0
    hi = len(array)

    while lo < hi:
        middle = lo + (hi - lo) // 2

        if array[middle] < search_key:
            lo = middle + 1
        else:
            hi = middle

    return lo


n, m = list(map(int, input().split()))
# n, m = list(map(int, "3 2".split()))

can_sizes_offered_by_shop = []
microlitres_needed_per_color = []

# can_sizes_offered_by_shop = [5, 7, 9]
# microlitres_needed_per_color = [6, 8]

microlitres_wasted = 0

for i in range(n):
    can_sizes_offered_by_shop.append(int(input()))

for i in range(m):
    microlitres_needed_per_color.append(int(input()))

can_sizes_offered_by_shop = sorted(can_sizes_offered_by_shop)

for m_needed in microlitres_needed_per_color:
    lower_bound_index = lower_bound(can_sizes_offered_by_shop, m_needed)
    microlitres_wasted += can_sizes_offered_by_shop[lower_bound_index] - m_needed

print(microlitres_wasted)