n = int(input())

instructions = [input() for _ in range(n)]
filtered_instructions = list(filter(lambda x: 'Simon says' in x, instructions))

for instruction in filtered_instructions:
    prefix_length = 11
    print(instruction[11:])
