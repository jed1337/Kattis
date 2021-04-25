input()
junk_per_day = list(map(int, input().split()))

least_junk = min(junk_per_day)
for i in range(len(junk_per_day)):
    if junk_per_day[i]==least_junk:
        print(i)
        break