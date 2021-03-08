fingering = {}
fingering[""] = {}
fingering["c"] = {2, 3, 4, 7, 8, 9, 10}
fingering["d"] = {2, 3, 4, 7, 8, 9}
fingering["e"] = {2, 3, 4, 7, 8}
fingering["f"] = {2, 3, 4, 7}
fingering["g"] = {2, 3, 4}
fingering["a"] = {2, 3}
fingering["b"] = {2}
fingering["C"] = {3}
fingering["D"] = {1, 2, 3, 4, 7, 8, 9}
fingering["E"] = {1, 2, 3, 4, 7, 8}
fingering["F"] = {1, 2, 3, 4, 7}
fingering["G"] = {1, 2, 3, 4}
fingering["A"] = {1, 2, 3}
fingering["B"] = {1, 2}

n = int(input())
for _ in range(n):
    song = input()
    presses = [0] * 11

    previous_note = ""
    for note in song:
        difference = fingering[note].difference(fingering[previous_note])
        for different in difference:
            if different in fingering[note]:
                presses[different] += 1
        previous_note = note

    result = " ".join(map(str, presses[1:]))
    print(result)
