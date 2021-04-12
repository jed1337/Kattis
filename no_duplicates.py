from collections import Counter

word_count = Counter(input().split())

has_duplicate = any(filter(lambda v: v > 1, word_count.values()))
if has_duplicate:
    print("no")
else:
    print("yes")
