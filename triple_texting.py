from collections import defaultdict

word = input()

dict = defaultdict(lambda: 0)
length = int(len(word)/3)
for i in range(3):
    start = i * length
    end = (i + 1) * length
    dict[word[start:end]]+=1

for k,v in dict.items():
    if v>1:
        print(k)
        break
