def mirror_image(image):
    for i in range(len(image)):
        image[i] = image[i][::-1]

    return image[::-1]


test_cases = int(input())
for i in range(test_cases):
    image = []
    rows, _ = list(map(int, input().split()))

    for j in range(rows):
        image.append(input())

    print("Test {}".format(i + 1))

    print("\n".join(mirror_image(image)))
