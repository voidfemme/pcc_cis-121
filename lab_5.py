__author__ = "Rose S Proctor"

# Program Description:
#	1. Prompts the user to input their first name
#	2. Converts the letters of user's first name to list of integers
#	3. Adds list of integers to determine passcode
#	4. Asks the user to input the passcode
#	5. Verifies the output is an integer
#	6. Verifies user input matches the code calculated by the program, Displays a hint if incorrect
#	7. Displays verification message

# Input List:
#	firstName
#	inputPasscode
# Output List
#	firstName
#	calculatedPasscode

############################################################################################################################
## Program Start ##
############################################################################################################################

class Hint:
	def __init__(self, hint):
		self.hint = hint
	
	def show(self):
		print(f"hint: {self.hint} ")

# Define String Function getFirstName()
#	Declare String firstName = "a"
# 	Display "Welcome to R.O.S.E, Reasoning Organization Subsystem Experiment"
#	Display ""
# 	Display "R.O.S.E.: Please state your first name >>> "
# 	Input String firstName
#	Display ""
#	Display "Hello, _",firstName,"_ Welcome."
#	Return String firstName
# End Module

def getFirstName():
	firstName = "a"
	print("Welcome to R.O.S.E, Reasoning.: Organization Subsystem Experiment")
	print("")
	firstName = input("R.O.S.E.: Please enter your first name >>> ")
	return firstName

# Define String Function getLastName()
#	Declare String firstName = "a"
# 	Display "Welcome to R.O.S.E, Reasoning Organization Subsystem Experiment"
#	Display ""
# 	Display "R.O.S.E.: Please state your first name >>> "
# 	Input String firstName
#	Display ""
#	Display "Hello, _",firstName,"_ Welcome."
#	Return String firstName
# End Module

def getLastName(firstName):
	lastName = "z"
	print("")
	lastName = input("R.O.S.E.: Please enter your last name >>> ")
	print("")
	print("Hello, _",firstName, lastName,"_ Welcome.")
	return lastName

# Define Integer Function lengthOfName(String name):
#	Set Integer numberOfLetters = len(name)
#	Return Integer numberOfLetters
# End Module

def lengthOfName(name):
	numberOfLetters = len(name)
	return numberOfLetters

# Define Integer Function multiplyPasscode(Integer multiplier, Integer calculatedPasscode)
#	Declare Integer multipliedPasscode = 0
# 	Set Integer multipliedPasscode = Integer multiplier * Integer calculatedPasscode
# 	Return Integer multipliedPasscode

def multiplyPasscode(multiplier, calculatedPasscode):
	multipliedPasscode = 0
	multipliedPasscode = multiplier * calculatedPasscode
	return multipliedPasscode

# Define List Function caesarCipher(String name)
#	Declare List convertedName []
#	Set String name lowercase
#	For letter in String name:
#		Set Integer number = ord(letter) - 96 				--## Set number to the unicode point for each letter in String firstName ##--
#		Append Integer number to List convertedName
#	End For
#	Return List convertedName
# End Module

def caesarCipher(name):
	convertedName = []
	name = name.lower()
	for letter in name:
		number = ord(letter) - 96
		convertedName.append(number)
	return convertedName

# Define Integer Function generatePasscode(List convertedFirstName)
#	Declare Integer calculatedPasscode = 0
#	For number in range(0, length(List convertedFirstName)):
#		Set Integer calculatedPasscode = Integer calculatedPasscode + List convertedFirstName[number]
#	End For
#	Return Integer calculatedPasscode
# End Module

def generatePasscode(listFromString):
	calculatedPasscode = 0
	for number in range(0, len(listFromString)):
		calculatedPasscode = calculatedPasscode + listFromString[number]
	return calculatedPasscode

# Define String Function inputPasscodeDialog()
#	Declare String inputPasscode
# 	Display "R.O.S.E.: I am R.O.S.E. I need your help to access my main processor."
# 	Display ""
# 	Display "a = 1, b = 2, c = 4, etc."
# 	Display "R.O.S.E.: Your name is the passcode."
# 	Display "R.O.S.E.: Please enter your passcode >>> "
#	Input String inputPasscode
#	Set Boolean is_valid = is_valid_integer(String inputPasscode)
#	While Not Boolean is_valid:
#		Display ""
# 		Display "Try again, not a valid integer >>> "
#		Input String inputPasscode
#		Set Boolean is_valid = is_valid_integer(String inputPasscode)
#	Return String inputPasscode
# End Module

def inputPasscodeDialog():
	inputPasscode = ""
	print("R.O.S.E.: I am R.O.S.E. I need your help to access my main processor.")
	print("")
	print("R.O.S.E.: Add the letters of your first name and multiply it by the number of letters in your last name.")
	inputPasscode = input("R.O.S.E.: Please enter your passcode >>> ")
	is_valid = is_valid_integer(inputPasscode)
	while not is_valid:
		print("")
		inputPasscode = input("Try again, not a valid integer >>> ")
		is_valid = is_valid_integer(inputPasscode)
	return inputPasscode

# Define Boolean Function is_valid_integer(String input_string)
#	Try:
#		Call Function int(String input_string)
#		Set Boolean is_valid = TRUE
#	Except ValueError:
#		Set Boolean is_valid = FALSE
#	Return Boolean is_valid
# End Module

def is_valid_integer(input_string):
	try:
		int(input_string)
		is_valid = True
	except ValueError:
		is_valid = False
	return is_valid

# Define Module authenticatePasscode(String inputPasscode, Integer calculatedPasscode)
#	While Integer inputPasscode - Integer calculatedPasscode != 0, Then
#		Display ""
#		Display "hint: your passcode is", calculatedPasscode
#		Display "Incorrect passcode, please try again >>> "
#		Input String inputPasscode
#		While Not Boolean is_valid:
#			Display ""
# 			Display "Try again, not a valid integer >>> "
#			Input String inputPasscode
#			Set Boolean is_valid = is_valid_integer(String inputPasscode)
#		End While
#	End While
#	Return
# End Module

def authenticatePasscode(inputPasscode, calculatedPasscoed, finalPasscode):
	attemptNum = 
	while int(inputPasscode) - finalPasscode != 0: 
		print(hints(attemptNum, calculatedPasscode, finalPasscode))
		inputPasscode = input("Incorrect passcode, please try again >>> ")
		attemptNum = attemptNum + 1
		is_valid = is_valid_integer(inputPasscode)
		while not is_valid:
			print("")
			inputPasscode = input("Try again, not a valid integer >>> ")
			is_valid = is_valid_integer(inputPasscode)
	return

def hints(attemptNum, calculatedPasscode, finalPasscode):
	counter = 0
	listOfHints = []

	hint1 = "a = 1, b = 2, c = 4, etc."
	hint2 = f"multiply {calculatedPasscode} with the number of letters in your last name."
	hint2 = f"your passcode is {finalPasscode}"

	listOfHints = [hint1, hint2, hint3]
	while counter <= len(listOfHints):
		hint = listOfHints[counter]
		counter = counter + 1
		if counter == len(listOfHints):
			counter = 0

	return hint


# what I need this to do is cycle through the possible hints.
# so if [counter] = len(listOfHints), It needs to loop
# while:
 

# Define Module passcodeAccepted()
#	Display ""
# 	Display "R.O.S.E.: Thank you. Your passcode has been accepted."										
# 	Display "R.O.S.E.: huh... *scratches head* I know I left my processor around here somewhere..."
# End Module

def passcodeAccepted():
	print("")
	print("R.O.S.E.: Thank you. Your passcode has been accepted.")
	print("R.O.S.E.: huh... *scratches head* I know I left my processor around here somewhere...")

# Define Module main()
#	Declare String firstName
#	Declare List convertedFirstName
#	Declare Integer calculatedPasscode
#	Declare String inputPasscode
#
#	Set String firstName = getFirstName()
#	Set List convertedFirstName = convertNameToNumberList(String firstName)
#	Set Integer calculatedPasscode = generatePasscode(List convertedFirstName)
#	Set String inputPasscode = inputPasscodeDialog()
#	Call authenticatePasscode(String inputPasscode, Integer calculatedPasscode)
#	Call passcodeAccepted
# End Module

def main():
	firstName = ""
	lastName = ""
	convertedFirstName = []
	lastNameInt = 0
	calculatedPasscode = 0
	finalPasscode = 0
	inputPasscode = 0

	firstName = getFirstName()
	lastName = getLastName(firstName)
	convertedFirstName = caesarCipher(firstName)
	lastNameInt = lengthOfName(lastName)
	calculatedPasscode = generatePasscode(convertedFirstName)
	finalPasscode = multiplyPasscode(lastNameInt, calculatedPasscode)
	inputPasscode = inputPasscodeDialog()
	authenticatePasscode(inputPasscode, calculatedPasscode, finalPasscode)
	passcodeAccepted()

# Call Module main()

main()