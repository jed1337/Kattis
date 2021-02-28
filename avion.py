blimps = [input() for _ in range(5)]

fbi_blimp_indexes = []
for i in range(len(blimps)):
    if "FBI" in blimps[i]:
        fbi_blimp_indexes.append(str(i+1))


if fbi_blimp_indexes:
    print(" ".join(fbi_blimp_indexes))
else:
    print("HE GOT AWAY!")