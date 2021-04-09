CHROMATIC_SCALE = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"] * 2


def get_major_scale(tonic):
    do = CHROMATIC_SCALE.index(tonic)
    re = do + 2
    mi = re + 2
    fa = mi + 1
    sol = fa + 2
    la = sol + 2
    ti = la + 2

    return [
        CHROMATIC_SCALE[do],
        CHROMATIC_SCALE[re],
        CHROMATIC_SCALE[mi],
        CHROMATIC_SCALE[fa],
        CHROMATIC_SCALE[sol],
        CHROMATIC_SCALE[la],
        CHROMATIC_SCALE[ti]
    ]


def exists_in_scale(notes, value):
    for note in notes:
        if note not in value:
            return False
    return True


SCALES = {
    "A": get_major_scale("A"),
    "A#": get_major_scale("A#"),
    "B": get_major_scale("B"),
    "C": get_major_scale("C"),
    "C#": get_major_scale("C#"),
    "D": get_major_scale("D"),
    "D#": get_major_scale("D#"),
    "E": get_major_scale("E"),
    "F": get_major_scale("F"),
    "F#": get_major_scale("F#"),
    "G": get_major_scale("G"),
    "G#": get_major_scale("G#")
}

input()
notes = list(set(input().split()))
exist_in_scale = []
for key, value in SCALES.items():
    if exists_in_scale(notes, value):
        exist_in_scale.append(key)

if exist_in_scale:
    print(" ".join(exist_in_scale))
else:
    print("none")