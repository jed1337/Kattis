string = input()

string_length = len(string)
whitespace_count = 0
lowercase_count = 0
uppercase_count = 0
symbol_count = 0

for char in string:
    if char == '_':
        whitespace_count += 1
    elif char.islower():
        lowercase_count += 1
    elif char.isupper():
        uppercase_count += 1
    elif char != '_':
        symbol_count += 1

print(whitespace_count/string_length)
print(lowercase_count/string_length)
print(uppercase_count/string_length)
print(symbol_count/string_length)