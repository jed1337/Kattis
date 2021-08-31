w, _ = list(map(int, input().split()))
partitions = list(map(int, input().split()))
partitions = [0] + partitions + [w]

widths = []
for i in range(len(partitions)):
    current_partition = partitions[i]
    for j in range(i+1, len(partitions)):
        other_partition = partitions[j]
        widths.append(other_partition-current_partition)

result = sorted(list(set(widths)))
print(" ".join(map(str, result)))
