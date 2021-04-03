students, throws = input().split()
students = int(students)
throws = int(throws)

egg_holder = 0
egg_holders = [0]

commands = input().split()
do_undo = False
for command in commands:
    if command == "undo":
        do_undo = True
    elif do_undo == True:
        undo_amount = int(command)
        for i in range(undo_amount):
            egg_holders.pop()
        egg_holder = egg_holders[-1]
        do_undo = False
    else:
        throw_amount = int(command)
        egg_holder = (throw_amount + egg_holder) % students

        egg_holders.append(egg_holder)

print(egg_holders[-1])