def main():
	letters = "abyz"
	numbers = []
	for letter in letters:
		number = ord(letter) - 96
		numbers.append(number)

	print(numbers)

main()

# Define module main()
#	Declare String letters "abyz"
#	Declare List numbers []
#	For letter in letters:
#		Set number = ord(letter) - 96
#		numbers.append(number)
#	Return numbers