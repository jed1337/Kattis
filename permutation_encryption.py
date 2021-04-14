import re


def zero_index(int_list):
    return list(map(lambda x: x - 1, int_list))


def pad_message(message, length):
    while len(message) % length != 0:
        message = message + " "

    return message


def encrypt(message, key):
    encrypted = ""
    for i in range(len(key)):
        encrypted += message[key[i]]

    return encrypted


while True:
    line = input()
    if line == '0':
        break

    key = list(map(int, line.split()))
    message = input()

    length, key = key[0], key[1:]
    key = zero_index(key)

    message = pad_message(message, length)
    grouped = re.findall('.' * length, message)

    encrypted_group = list(map(lambda x: encrypt(x, key), grouped))

    print("'{}'".format(''.join(encrypted_group)))
