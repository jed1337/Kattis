name = input()

short_name = []
for letter in name:
    if short_name:
        if short_name[-1] != letter:
            short_name.append(letter)
    else:
        short_name.append(letter)
print("".join(short_name))