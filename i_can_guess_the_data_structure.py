import heapq
from collections import deque, Counter

STACK_INDEX = 0
QUEUE_INDEX = 1
HEAP_INDEX = 2


def get_data_structure_type(n):
    stack = deque()  # append, pop
    queue = deque()  # append, popleft
    heap = []  # heapq.heappush, heapq.heappop

    data_structure_type = [True, True, True]

    for _ in range(n):
        opcode, value = list(map(int, input().split()))
        if opcode == 1:
            stack.append(value)
            queue.append(value)
            heapq.heappush(heap, -value)
        else:
            if len(stack) == 0:
                data_structure_type = [False, False, False]
                continue

            s_result = stack.pop()
            q_result = queue.popleft()
            h_result = -heapq.heappop(heap)

            if s_result != value:
                data_structure_type[STACK_INDEX] = False
            if q_result != value:
                data_structure_type[QUEUE_INDEX] = False
            if h_result != value:
                data_structure_type[HEAP_INDEX] = False

    return data_structure_type


try:
    while True:
        n = int(input())
        data_structure_type = get_data_structure_type(n)

        counter = Counter(data_structure_type)
        if counter[False] == 3:
            print("impossible")
        elif counter[True] > 1:
            print("not sure")
        elif data_structure_type[STACK_INDEX]:
            print("stack")
        elif data_structure_type[QUEUE_INDEX]:
            print("queue")
        else:
            print("priority queue")
except EOFError:
    pass
