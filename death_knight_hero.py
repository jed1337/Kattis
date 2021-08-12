n = int(input())
battles = [input() for _ in range(n)]
wins = len(list(filter(lambda battle: 'CD' not in battle, battles)))
print(wins)
