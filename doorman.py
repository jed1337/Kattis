limit = int(input())
people = input()

turn_to_numbers = lambda x: 1 if x == "M" else -1
people = list(map(turn_to_numbers, people))

difference = 0
can_enter_club = 0
count = len(people)
for _ in range(count - 1):
    first_person = people[0]
    second_person = people[1]

    if abs(difference + first_person) > limit and abs(difference + second_person) > limit:
        break
    elif abs(difference + first_person) <= limit:
        difference += first_person
        can_enter_club += 1
        del people[0]
    elif abs(difference + second_person) <= limit:
        difference += second_person
        can_enter_club += 1
        del people[1]

if len(people) == 1:
    first_person = people[0]
    if abs(difference + first_person) <= limit:
        difference += first_person
        can_enter_club += 1
        del people[0]

print(can_enter_club)
