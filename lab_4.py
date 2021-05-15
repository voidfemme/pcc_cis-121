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
#	first_name
#	input_passcode
# Output List
#	first_name
#	calculated_passcode

############################################################################################################################
## Program Start ##
############################################################################################################################

# Define Module get_first_name()
#	Declare String first_name = "a"
# 	Display "Welcome to R.O.S.E, Reasoning Organization Subsystem Experiment"
#	Display ""
# 	Display "R.O.S.E.: Please state your first name >>> "
# 	Input String first_name
#	Display ""
#	Display "Hello, _",first_name,"_ Welcome."
#	Return String first_name
# End Module

def get_first_name():
	first_name = "a"
	print("Welcome to R.O.S.E, Reasoning.: Organization Subsystem Experiment")
	print("")
	first_name = input("R.O.S.E.: Please enter your first name >>> ")
	print("")
	print("Hello, _",first_name,"_ Welcome.")
	return first_name

# Define Module convert_name_to_number_list(String first_name)
#	Declare List converted_name_list []
#	Set String first_name lowercase
#	For letter in String first_name:
#		Set Integer number = ord(letter) - 96 				--## Set number to the unicode point for each letter in String first_name ##--
#		Append Integer number to List converted_name_list
#	End For
#	Return List converted_name_list
# End Module

def convert_name_to_number_list(first_name):
	converted_name_list = []
	first_name = first_name.lower()
	for letter in first_name:
		number = ord(letter) - 96
		converted_name_list.append(number)
	return converted_name_list

# Define Module generate_passcode(List converted_name_list)
#	Declare Integer calculated_passcode = 0
#	For number in range(0, length(List converted_name_list)):
#		Set Integer calculated_passcode = Integer calculated_passcode + List converted_name_list[number]
#	End For
#	Return Integer calculated_passcode
# End Module

def generate_passcode(converted_name_list):
	calculated_passcode = 0
	for number in range(0, len(converted_name_list)):
		calculated_passcode = calculated_passcode + converted_name_list[number]
	return calculated_passcode

# Define Module input_passcode_dialog()
#	Declare String input_passcode
# 	Display "R.O.S.E.: I am R.O.S.E. I need your help to access my main processor."
# 	Display ""
# 	Display "a = 1, b = 2, c = 4, etc."
# 	Display "R.O.S.E.: Your name is the passcode."
# 	Display "R.O.S.E.: Please enter your passcode >>> "
#	Input String input_passcode
#	Set Boolean is_valid = is_valid_integer(String input_passcode)
#	While Not Boolean is_valid:
#		Display ""
# 		Display "Try again, not a valid integer >>> "
#		Input String input_passcode
#		Set Boolean is_valid = is_valid_integer(String input_passcode)
#	Return String input_passcode
# End Module

def input_passcode_dialog():
	input_passcode = ""
	print("R.O.S.E.: I am R.O.S.E. I need your help to access my main processor.")
	print("")
	print("a = 1, b = 2, c = 4, etc.")
	print("R.O.S.E.: Your name is the passcode.")
	input_passcode = input("R.O.S.E.: Please enter your passcode >>> ")
	is_valid = is_valid_integer(input_passcode)
	while not is_valid:
		print("")
		input_passcode = input("Try again, not a valid integer >>> ")
		is_valid = is_valid_integer(input_passcode)
	return input_passcode

# Define Module is_valid_integer(String input_string)
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

# Define Module authenticate_passcode(String input_passcode, Integer calculated_passcode)
#	While Integer input_passcode - Integer calculated_passcode != 0, Then
#		Display ""
#		Display "hint: your passcode is", calculated_passcode
#		Display "Incorrect passcode, please try again >>> "
#		Input String input_passcode
#		While Not Boolean is_valid:
#			Display ""
# 			Display "Try again, not a valid integer >>> "
#			Input String input_passcode
#			Set Boolean is_valid = is_valid_integer(String input_passcode)
#		End While
#	End While
#	Return
# End Module

def authenticate_passcode(input_passcode, calculated_passcode):
	while int(input_passcode) - calculated_passcode != 0:
		print("")
		print("hint: your passcode is", calculated_passcode)
		input_passcode = input("Incorrect passcode, please try again >>> ")
		is_valid = is_valid_integer(input_passcode)
		while not is_valid:
			print("")
			input_passcode = input("Try again, not a valid integer >>> ")
			is_valid = is_valid_integer(input_passcode)
	return

# Define Module passcode_accepted()
#	Display ""
# 	Display "R.O.S.E.: Thank you. Your passcode has been accepted."										
# 	Display "R.O.S.E.: huh... *scratches head* I know I left my processor around here somewhere..."
# End Module

def passcode_accepted():
	print("")
	print("R.O.S.E.: Thank you. Your passcode has been accepted.")
	print("R.O.S.E.: huh... *scratches head* I know I left my processor around here somewhere...")

# Module main()
#	Declare String first_name
#	Declare List converted_name_list
#	Declare Integer calculated_passcode
#	Declare String input_passcode
#
#	Set String first_name = get_first_name()
#	Set List converted_name_list = convert_name_to_number_list(String first_name)
#	Set Integer calculated_passcode = generate_passcode(List converted_name_list)
#	Set String input_passcode = input_passcode_dialog()
#	Call authenticate_passcode(String input_passcode, Integer calculated_passcode)
#	Call passcode_accepted
# End Module

def main():
	first_name = ""
	converted_name_list = []
	calculated_passcode = 0
	input_passcode = 0

	first_name = get_first_name()
	converted_name_list = convert_name_to_number_list(first_name)
	calculated_passcode = generate_passcode(converted_name_list)
	input_passcode = input_passcode_dialog()
	authenticate_passcode(input_passcode, calculated_passcode)
	passcode_accepted()

# Call Module main()

main()