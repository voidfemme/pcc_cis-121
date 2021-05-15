# def hints():
	# counter = 0
	# listOfHints = []

	# hint1 = "a = 1, b = 2, c = 4, etc."
	# hint2 = f"multiply {calculatedPasscode} with the number of letters in your last name."
	# hint2 = f"your passcode is {finalPasscode}"

	# listOfHints = [hint1, hint2, hint3]
	# while counter <= len(listOfHints):
		# hint = listOfHints[counter]
		# counter = counter + 1
		# if counter == len(listOfHints):
			# counter = 0


def inputGuess():
	guess = input("enter 15: ")
	isValid = isValidInteger(guess)
	while not isValid:
			print("")
			guess = input("Try again, not a valid integer >>> ")
			isValid = isValidInteger(guess)
	return guess

def isValidInteger(inputString):
	try:
		int(inputString)
		isValid = True
	except ValueError:
		isValid = False
	return isValid

def cycleHints(guess):
	hintsList = []
	hint1 = "hint number 1"
	hint2 = "hint number 2"
	hint3 = "hint number 3"
	hintsList = [hint1, hint2, hint3]
	counter = 0

	while int(guess) - 15 != 0:
		print(hintsList[counter])
		guess = input("Incorrect passcode, please try again >>> ")
		isValid = isValidInteger(guess)
		while not isValid:
			print("")
			guess = input("Try again, not a valid integer >>> ")
			isValid = isValidInteger(guess)
		counter = counter + 1
		if counter == 3:
			counter = 0
		else:
			pass

def main():
	guess = 0
	guess = inputGuess()
	cycleHints(guess)
	print("success!")

main()


		# while attempt[0] <=3:
			# print(hint)
			# inputGuess = int(input("incorrect, try again: ")
			# attempt = attempt[1] + 1
			# print(hints(attempt[1]))
			# isValid = isValidInteger(inputGuess)
			# while not isValid:
				# inputGuess = input("non-Integer, try again: ")
				# isValid = isValidInteger(inputGuess)



# def hints(whichHint):
# 	hintsList = []
# 	hint = ""

# 	hint1 = "hint number 1"
# 	hint2 = "hint number 2"
# 	hint3 = "hint number 3"
# 	hintsList = [hint1, hint2, hint3]

# 	while whichHint >= len(hintsList):
# 			hint = hintsList[whichHint]
# 			whichHint = whichHint + 1
# 	if whichHint == len(hintsList):
# 		whichHint = 0
# 	return hint

