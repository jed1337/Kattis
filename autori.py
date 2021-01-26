names = input().split("-")
initials = [name[0].upper() for name in names]
print("".join(initials))