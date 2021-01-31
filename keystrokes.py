# https://open.kattis.com/problems/lyklagangriti
# Wrong answer on arnarLLLBBun
# Actual output = "unaar"
# Expected output = "unnar"


obfuscated = input()

cursor_index = 0
password_list = []
for char in obfuscated:
    if char == "L":
        cursor_index -= 1
    elif char == "R":
        cursor_index += 1
    elif char == "B":
        del password_list[cursor_index]
        cursor_index -= 1
    else:
        password_list.insert(cursor_index, char)
        cursor_index += 1

print("".join(password_list))