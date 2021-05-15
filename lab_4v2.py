__author__ = "Rose S Proctor"

# Program Description:
#	1. Prompts the user to input their first name
#	2. Converts the letters of user's first name to list of integers
#	3. Adds list of integers to determine passcode, and displays that passcode
#	4. Asks the user to input the passcode
#	5. Verifies the output is an integer
#	6. Verifies user input matches the code calculated by the program
#	7. Displays verification message

# Checklist
#	At least one input AND one output
#	Validate user input
#	Two loops, in meaningful ways
#	Separate modules
#	Use parameters, not global values
# 	Full Pseudocode
#	Input list:
#		first_name
#		input_passcode
#	Output list:
#		calculated_passcode

############################################################################################################################
## Program Start ##
############################################################################################################################

# Define Module get_first_name()
#	Declare String first_name = "a"
# 	Display "Welcome to R.O.S.E, Reasoning Organization Subsystem Experiment"
# 	Display "R.O.S.E: Please state your first name: "
# 	Input first_name
#	Display "Hello, ", first_name ". Welcome."
#	Return first_name
# End Module

def get_first_name():
	first_name = "a"
	print("Welcome to R.O.S.E, Reasoning Organization Subsystem Experiment")
	print("")
	first_name = input("R.O.S.E: Please state your first name >>> ")
	print("Hello, _",first_name,"_ Welcome.")
	return first_name

# Define Module convert_name_to_number_list(first_name)
#	Declare List name_index []
#	Set name = first_name
#	Set String name lowercase
#	For letter in name:
#		Set number = ord(letter) - 96
#		Append name_index to List name_index ## name_index.append(number) ##
#	Return name_index
# End Module

def convert_name_to_number_list(first_name):
	name_index = []
	name = first_name
	name = name.lower()
	for letter in name:
		number = ord(letter) - 96
		name_index.append(number)
	return name_index

# Define Module generate_passcode(name_index)
#	Declare Integer calculated_passcode = 0
#	Set list1 = numbers
#	For number in range(0, len(list1)):
#		calculated_passcode = calculated_passcode + list1[number]
#	End For
#	Return calculated_passcode
# End Module

def generate_passcode(name_index):
	calculated_passcode = 0
	list1 = name_index
	for number in range(0, len(list1)):
		calculated_passcode = calculated_passcode + list1[number]
	return calculated_passcode

# Define Module input_passcode_dialog()
#	Declare Integer input_passcode
# 	Display "R.O.S.E: I am R.O.S.E. I need your help to access my main processor."
# 	Display "a = 1, b = 2, c = 4, etc."
# 	Display "R.O.S.E: Your name is the passcode."
# 	Display "R.O.S.E: Please enter your passcode: "
#	Input input_passcode
#	Set is_valid = is_valid_integer(input_passcode)
#	While Not is_valid
#		Display "Try again, not a valid integer: "
#		Input input_passcode
#		is_valid = is_valid_integer(input_passcode)
#	Return input_passcode
# End Module

def input_passcode_dialog():
	input_passcode = ""
	print("")
	print("R.O.S.E: I am R.O.S.E. I need your help to access my main processor.")
	print("")
	print("a = 1, b = 2, c = 4, etc.")
	print("R.O.S.E: Your name is the passcode.")
	input_passcode = input("R.O.S.E: Please enter your passcode >>> ")
	is_valid = is_valid_integer(input_passcode)
	while not is_valid:
		print("")
		input_passcode = input("Try again, not a valid integer >>> ")
		is_valid = is_valid_integer(input_passcode)
	return input_passcode

# Define Module is_valid_integer(input_string)
#	Try:
#		Set String value = int(input_string)
#		Set Boolean is_valid = True
#	Except Value Error
#		Set Boolean is_valid = False
#	Return Boolean is_valid
# End Module

def is_valid_integer(input_string):
	try:
		int(input_string)
		is_valid = True
	except ValueError:
		is_valid = False
	return is_valid

# Define Module authenticate_passcode(input_passcode, calculated_passcode)
#	While Integer input_passcode - Integer calculated_passcode != 0, Then
#		Display "Incorrect passcode, please try again"
#		Input input_passcode
#	Return
# End Module

def authenticate_passcode(input_passcode, calculated_passcode):
	while int(input_passcode) - calculated_passcode != 0:
		print("")
		print("hint: your passcode is", calculated_passcode)
		input_passcode = input("Incorrect passcode, please try again >>> ")
	return

# Define Module passcode_accepted()
# 	Display "R.O.S.E: Thank you. Your passcode has been accepted."										
# 	Display "R.O.S.E: huh... *scratches head* I know I left my processor around here somewhere..."
# End Module

def passcode_accepted():
	print("")
	print("R.O.S.E: Thank you. Your passcode has been accepted.")
	print("R.O.S.E: huh... *scratches head* I know I left my processor around here somewhere...")

# Module main()
#	first_name = ""
#	name_index = []
#	calculated_passcode = 0
#	input_passcode = ""
#	Set String first_name = get_first_name()
#	Set List name_index = convert_name_to_number_list(first_name)
#	Set calculated_passcode = generate_passcode(name_index)
#	Set input_passcode = input_passcode_dialog()
#	Call passcode_accepted
# End Module

def main():
	first_name = ""
	name_index = []
	calculated_passcode = 0
	input_passcode = 0
	first_name = get_first_name()
	name_index = convert_name_to_number_list(first_name)

	calculated_passcode = generate_passcode(name_index)
	input_passcode = input_passcode_dialog()

	authenticate_passcode(input_passcode, calculated_passcode)
	passcode_accepted()

main()


# # ##[draft]##
# # Define Module main()
# #	get_name()
# #	convert_name_to_list()
# #	add_list_to_make_passcode()
# #	get_passcode_guess()


# #	is_passcode_integer()


# #	verify_passcode_guess
# #	passcode_accepted()