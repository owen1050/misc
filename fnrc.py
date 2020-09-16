input = "abccddddeeeeeffffg"


def firstNonRepeatingCharacter(input):
	letterCount = {}
	for letter in input:
		if letter in letterCount:
			letterCount[letter] = letterCount[letter]+1
		else:
			letterCount[letter] = 1

	for letter in input:
		if letterCount[letter] == 1:
			return letter

print(firstNonRepeatingCharacter(input))