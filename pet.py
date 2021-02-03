all_scores = {}
for i in range(1, 6):
    score = sum(list(map(int, input().split())))
    all_scores[i] = score

max_score = 0
team = 1
for i in range(1, 6):
    team_score = all_scores[i]
    if team_score > max_score:
        max_score = team_score
        team = i

print(team, max_score)
