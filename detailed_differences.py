n = int(input())

for _ in range(n):
    string1 = input()
    string2 = input()

    result = []
    for i in range(len(string1)):
        if string1[i]==string2[i]:
            result.append(".")
        else:
            result.append("*")

    print(string1)
    print(string2)
    print("".join(result))
    print()

