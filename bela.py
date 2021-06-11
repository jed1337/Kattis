value_table = {}
value_table['A'] = (11, 11)
value_table['K'] = (4, 4)
value_table['Q'] = (3, 3)
value_table['J'] = (20, 2)
value_table['T'] = (10, 10)
value_table['9'] = (14, 0)
value_table['8'] = (0, 0)
value_table['7'] = (0, 0)

n, dominant_suit = input().split()
n = int(n)

cards = [input() for _ in range(n * 4)]

points = 0
for card in cards:
    number, suit = card[0], card[1]
    if suit == dominant_suit:
        points += value_table[number][0]
    else:
        points += value_table[number][1]

print(points)
