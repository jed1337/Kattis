def get_closest_sum(integers, query):
    closest_sum = int(1e9)
    difference = int(1e9)

    for i in range(len(integers)):
        for j in range(i + 1, len(integers)):
            sum = integers[i] + integers[j]
            if abs(query - sum) < difference:
                difference = abs(query - sum)
                closest_sum = sum
    return closest_sum


try:
    case_number = 1
    while True:
        n = int(input())
        integers = [int(input()) for _ in range(n)]
        m = int(input())
        queries = [int(input()) for _ in range(m)]

        print("Case {}:".format(case_number))
        for query in queries:
            closest_sum = get_closest_sum(integers, query)
            print("Closest sum to {} is {}.".format(query, closest_sum))

        case_number += 1

except EOFError:
    pass
