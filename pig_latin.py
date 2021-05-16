from sys import stdin
vowels = "aeiouy"

def pig_latin(lines):
	pig_latin_lines=[]
	for line in lines.split():
		line = line.strip()
		if line[0] in vowels:
			pig_latin_lines.append(line+"yay")
		else:
			first_vowel_index = -1
			for i in range(len(line)):
				if line[i] in vowels:
					first_vowel_index = i
					break
			pig_latin_lines.append(line[first_vowel_index:] + line[0:first_vowel_index] + "ay")
	return " ".join(pig_latin_lines)


for line in stdin:
    if line == '':
        break
    print(pig_latin(line))
    