# Algorithm
# Subtract 12 from the wire length to simplify
# Subtract 6 from bird positions because we subtracted from the wire
# While we can still fit more birds
# Start from the left most
# If we can fit a bird, place it there
# Else If we can't since another bird is already there or if we'll hit the spacing limit
#   Set the place to add birds from to the current bird

def solve(wire_length, bird_spacing, bird_positions):
    if wire_length <= 0:
        return 0

    i = 0
    bird_index = 0
    additional_bird_count = 0
    while i <= wire_length:
        if bird_index < len(bird_positions):
            spacing = i + bird_spacing
            if spacing < bird_positions[bird_index] and spacing < wire_length:
                additional_bird_count += 1
            else:
                i = bird_positions[bird_index]
                bird_index += 1
        elif i <= wire_length:
            additional_bird_count += 1

        i += bird_spacing

    return additional_bird_count


wire_length, bird_spacing, bird_count = list(map(int, input().split()))

# Subtract the length that we can't go to
wire_length -= 12

# Move the birds back 6 positions since we subtracted the wire length
bird_positions = [int(input()) - 6 for _ in range(bird_count)]
bird_positions.sort()

print(solve(wire_length, bird_spacing, bird_positions))
