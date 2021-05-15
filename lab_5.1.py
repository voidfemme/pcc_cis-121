__author__ = "Rose S Proctor"

# Program Description:
#	1. Prompts the user to input their first and last name.
#	2. Transforms  and stores the previously input full name 
#		into an Integer value.
#	4. Presents the user with a riddle.
#	5. Verifies the user input is a valid integer.
#	6. Verifies user input matches the answer as calculated 
# 		by the program, Displays a consecutive list of 
# 		hints if incorrect.
#	7. Displays verification message.

# Input List:
#	name
#	userPasscode
# Output List
#	inputMessage
# 	hintsList[counter]

############################################################
## Program Start ##
############################################################

# Define List Module getFullName():
# 	Declare names = []
# 	Declare String firstName = ""
# 	Declare String lastName = ""
# 	Display "Welcome to R.O.S.E, Reasoning Organization Subsystem Experiment"
# 	Display ""
# 	Set String firstName = getName("first")
# 	Set String lastName = getName("last")
# 	Set List names = [String firstName, String lastName]
# 	Display ""
# 	Display "Hello, _",firstName, lastName,"_ Welcome."
# 	Return List names
# End Module

def getFullName():
	names = []
	firstName = ""
	lastName = ""
	print("Welcome to R.O.S.E, Reasoning Organization Subsystem Experiment")
	print("")
	firstName = getName("first")
	lastName = getName("last")
	names = [firstName, lastName]
	print("")
	print("Hello, _",firstName, lastName,"_ Welcome.")
	return names

# Define String Function getName(String whichName):
# 	Declare String inputMessage = ""
# 	Set String inputMessage = "R.O.S.E.: Please enter your " + whichName + " name >>> "
# 	Display String inputMessage
# 	Return String name
# End Function

def getName(whichName):
	inputMessage = ""
	inputMessage = "R.O.S.E.: Please enter your " + whichName + " name >>> "
	name = input(inputMessage)
	return name

# Define List Function caesarCipher(String firstName):
# 	Declare List caesarCipher = []
# 	Set String firstName = lowercase String firstName
# 	For String letter in String firstName:
# 		Set Integer number = ord(String letter) - 96
# 		Append String Number to List caesarCipher
#	End For
# 	Return List caesarCipher
# End Function

def caesarCipher(firstName):
	caesarCipher = []
	firstName = firstName.lower()
	for letter in firstName:
		number = ord(letter) - 96
		caesarCipher.append(number)
	return caesarCipher

# Define Integer Function addIntegerList(List integerList):
# 	Declare Integer caesarCipherSum = 0
# 	For Integer number in range(0, len(List integerList)):
# 		Set Integer caesarCipherSum = Integer caesarCipherSum + Integer integerList[number]
# 	End For
# 	Return Integer caesarCipherSum
# End Function

def addIntegerList(integerList):
	caesarCipherSum = 0
	for number in range(0, len(integerList)):
		caesarCipherSum = caesarCipherSum + integerList[number]
	return caesarCipherSum

# Define String Function inputPasscode():
# 	Declare String userPasscode = ""
#	Declare Boolean isValid

# 	Display "R.O.S.E.: I am R.O.S.E. I need your help to access my main processor."
# 	Display ""
# 	Display "R.O.S.E.: (y+o+u+r+f+i+r+s+t+n+a+m+e)*your_last_name_length to determine your passcode."
# 	Display "R.O.S.E.: Please enter your passcode >>> "
# 	Input Integer userPasscode
# 	Set Boolean isValid = isValidInteger(userPasscode)

# 	While not isValid
# 		Display "")
# 		Display "Try again, not a valid integer >>> ")
# 		Input String userPasscode
# 		Set Boolean isValid = isValidInteger(Integer userPasscode)
#	End While
# 	return String userPasscode
# End Function

def inputPasscode():
	userPasscode = ""
	isValid = False

	print("R.O.S.E.: I am R.O.S.E. I need your help to access my main processor.")
	print("")
	print("R.O.S.E.: (y+o+u+r+f+i+r+s+t+n+a+m+e)*your_last_name_length to determine your passcode.")
	userPasscode = input("R.O.S.E.: Please enter your passcode >>> ")
	isValid = isValidInteger(userPasscode)
	while not isValid:
		print("")
		userPasscode = input("Try again, not a valid integer >>> ")
		isValid = isValidInteger(userPasscode)
	return userPasscode

# Define Boolean Function isValidInteger(String inputString):
# 	Try
# 		Integer inputString
# 		Set Boolean isValid = True
# 	Except ValueError:
# 		Set Boolean isValid = False
#	End Try
# 	Return Boolean isValid
# End Module

def isValidInteger(inputString):
	try:
		int(inputString)
		isValid = True
	except ValueError:
		isValid = False
	return isValid

# Define Module authenticatePasscode(Integer lastNameLength, Integer firstNameSum, Integer userPasscode, Integer generatedPasscode):
# 	Declare List hintsList = []
# 	Declare String hint1 = "a = 1, b = 2, c = 4, etc."
# 	Declare String hint2 = "multiply " + str(stringLength) + " by " + str(stringSum)
# 	Declare String hint3 = "your passcode is " + str(generatedPasscode)
# 	Set List hintsList = [hint1, hint2, hint3]
# 	Set Integer counter = 0
#	Set Boolean isValid = False
# 	While Integer userPasscode - Integer generatedPasscode != 0:
# 		Display""
# 		Display"hint: ", hintsList[counter]
#		Display "Incorrect passcode, please try again >>> "
# 		Input userPasscode
# 		Set Boolean isValid = isValidInteger(Integer userPasscode)
# 		While not isValid
# 			Display ""
#			Display "Try again, not a valid integer >>> "
# 			Input userPasscode
# 			Set Boolean isValid = isValidInteger(Integer userPasscode)
# 		End While
# 		Set Integer counter = Integer counter + 1
# 		If Integer counter == 3:
# 			Set Integer counter = 0
# 		Else
# 			Pass
#		End If
#	End While
# End Module

def authenticatePasscode(stringLength, stringSum, userPasscode, generatedPasscode):
	hintsList = []
	hint1 = "a = 1, b = 2, c = 4, etc."
	hint2 = "multiply " + str(stringLength) + " by " + str(stringSum)
	hint3 = "your passcode is " + str(generatedPasscode)
	hintsList = [hint1, hint2, hint3]
	counter = 0
	isValid = False
	while int(userPasscode) - generatedPasscode != 0:
		print("")
		print("hint: ", hintsList[counter])
		userPasscode = input("Incorrect passcode, please try again >>> ")
		isValid = isValidInteger(userPasscode)
		while not isValid:
			print("")
			userPasscode = input("Try again, not a valid integer >>> ")
			isValid = isValidInteger(userPasscode)
		counter = counter + 1
		if counter == 3:
			counter = 0
		else:
			pass

# Define Module passcodeAccepted():
	# Display ""
	# Display "R.O.S.E.: Thank you. Your passcode has been accepted."
	# Display "R.O.S.E.: huh... *scratches head* I know I left my processor around here somewhere..."
# End Module

def passcodeAccepted():
	print("")
	print("R.O.S.E.: Thank you. Your passcode has been accepted.")
	print("R.O.S.E.: huh... *scratches head* I know I left my processor around here somewhere...")

# Define Module main()
# 	Declare List fullName = []
# 	Declare List firstNameNumberList = []
# 	Declare Integer lastNameLength = 0
# 	Declare Integer firstNameSum = 0
# 	Declare Integer userPasscode = 0
# 	Declare Integer generatedPasscode = 0

# 	Set List fullName = getFullName()
# 	Set List firstNameNumberList = caesarCipher(String fullName[0])
# 	Set Integer firstNameSum = addIntegerList(List firstNameNumberList)
# 	Set Integer lastNameLength = len(String fullName[1])
# 	Set Integer generatedPasscode = Integer lastNameLength * Integer firstNameSum
# 	Set Integer userPasscode = inputPasscode()
# 	Call Module authenticatePasscode(Integer lastNameLength, Integer firstNameSum, Integer userPasscode, Integer generatedPasscode)
# 	Call Module passcodeAccepted()
# End Module

def main():
	fullName = []
	firstNameNumberList = []
	lastNameLength = 0
	firstNameSum = 0
	userPasscode = 0
	generatedPasscode = 0

	fullName = getFullName()
	firstNameNumberList = caesarCipher(fullName[0])
	firstNameSum = addIntegerList(firstNameNumberList)
	lastNameLength = len(fullName[1])
	generatedPasscode = lastNameLength * firstNameSum
	print("DEBUGMSG:", generatedPasscode)	
	userPasscode = inputPasscode()
	authenticatePasscode(lastNameLength, firstNameSum, userPasscode, generatedPasscode)
	passcodeAccepted()

# Call Module main()

main()