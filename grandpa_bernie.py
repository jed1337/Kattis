from collections import defaultdict

country_dict = defaultdict(lambda: [])
for _ in range(int(input())):
    country, year = input().split()
    year = int(year)
    country_dict[country].append(year)

for k, v in country_dict.items():
    country_dict[k].sort()

for _ in range(int(input())):
    country, time = input().split()
    time = int(time) - 1
    print(country_dict[country][time])
