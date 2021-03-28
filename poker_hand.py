from collections import Counter

hands = Counter([hand[0:1] for hand in input().split()])
print(max(hands.values()))
