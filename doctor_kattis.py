"""
A heap is used to order the patients by infection level, then arrival time at the clinic
"""

import heapq

INFECTION_INDEX = 0
ARRIVAL_INDEX = 1
NAME_INDEX = 2

command_count = int(input())

arrive_time = 0
patient_heap = []
for _ in range(command_count):
    command = input().split()
    opcode = command[0]
    if opcode == "0":
        _, name, infection = command
        # Store the infection in negative so that the most infected will be at the first
        heapq.heappush(patient_heap, [-int(infection), int(arrive_time), name])
        arrive_time += 1
    elif opcode == "1":
        _, name, increase_value = command
        for i in range(len(patient_heap)):
            if patient_heap[i][NAME_INDEX] == name:
                patient_heap[i][INFECTION_INDEX] -= int(increase_value)
                heapq.heapify(patient_heap)
                break
    elif opcode == "2":
        _, name = command
        for i in range(len(patient_heap)):
            if patient_heap[i][NAME_INDEX] == name:
                del patient_heap[i]
                heapq.heapify(patient_heap)
                break
    elif opcode == "3":
        if patient_heap:
            print(patient_heap[0][NAME_INDEX])
        else:
            print("The clinic is empty")
