__author__ = "Rose S Proctor"

# This program is a story about an AI.

# Checklist
#	At least one input AND one output
#	Validate user input
#	Two loops, in meaningful ways
#	Separate modules
#	Use parameters, not global values

# Full Pseudocode

############################################################################################################################
## Program Start ##
############################################################################################################################

# Define Module get_first_name()
#	Declare String first_name = "a"
# 	Display "Welcome to R.O.S.E, Reasoning Organization Subsystem Experiment"
# 	Display "R.O.S.E: Please state your first name: "
# 	Input first_name
#	Display "Hello, " first_name ". Welcome."
#	Return first_name
# End Module

def get_first_name():
	first_name = "a"
	print("Welcome to R.O.S.E, Reasoning Organization Subsystem Experiment")
	first_name = input(str("R.O.S.E: Please state your first name: "))
	print("Hello, ", first_name, ". Welcome.")
	return first_name

# Define Module cipher(first_name)
#	Declare List name_index []
#	Set name = first_name
#	Set String name lowercase
#	For letter in name:
#		Set number = ord(letter) - 96
#		Append name_index to List name_index ## name_index.append(number) ##
#	Return name_index
# End Module

def cipher(first_name):
	name_index = []
	name = first_name
	name = name.lower()
	for letter in name:
		number = ord(letter) - 96
		name_index.append(number)
	print("DEBUGG 01: ",name_index)
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
	name_numbers = name_index
	for number in range(0, len(name_numbers)):
		calculated_passcode = calculated_passcode + name_numbers[number]
	print("DEBUGG 02: ", calculated_passcode)
	return calculated_passcode

# Define Module input_passcode_dialog()
#	Declare Integer input_passcode
# 	Display "R.O.S.E: I am R.O.S.E. I need your help to access my main processor."
# 	Display "a = 1, b = 2, c = 4, etc."
# 	Display "R.O.S.E: Your name is the input_passcode."
# 	Display "R.O.S.E: Please enter your input_passcode."
#	Input input_passcode
#	Return input_passcode
# End Module

def input_passcode_dialog():
	input_passcode = ""
	print("R.O.S.E: I am R.O.S.E. I need your help to access my main processor.")
	print("a = 1, b = 2, c = 4, etc.")
	print("R.O.S.E: The sum of your name is the passcode.")
	input_passcode = input("R.O.S.E: Please enter your passcode.")
	return input_passcode

# def is_passcode_integer(input_passcode):
# 	try:
# 		val = int(input_passcode)
# 		is_valid = True
# 	except ValueError:
# 		is_valid = False
# 	return is_valid

# def is_passcode_integer(input_passcode):
# 	try:
# 		is_valid = int(input_passcode)
# 		is_valid = True
# 		print("try")
# 	except ValueError:
# 		is_valid = False
# 		print("except ValueError")
# 	return is_valid

# Define Module authenticate_passcode(is_valid, calculated_passcode)
# 	If is_valid - calculated_passcode != 0 Then
#		Display "Incorrect passcode! Try again: "
#		Input is_valid
#		Set is_valid = input
#	Else
#		Return
# End Module

def authenticate_passcode(input_passcode, calculated_passcode):
	if input_passcode - calculated_passcode == 0:
		input_passcode = input("Incorrect passcode! Try again: ")
	else:
		return
		

# Define Module passcode_accepted()
# 	Display "R.O.S.E: Thank you. Your passcode has been accepted."										
# 	Display "R.O.S.E: huh... *scratches head* I know I left my processor around here somewhere..."
# End Module

def passcode_accepted():
	print("R.O.S.E: Thank you. Your passcode has been accepted.")
	print("R.O.S.E: huh... *scratches head* I know I left my processor around here somewhere...")

# Module main()
#	Declare String first_name "a"
#	Declare List name_index []
#	Declare Integer calculated_passcode 0
#	Declare String input_passcode ""
#	Declare Integer is_valid
#
# 	Set first_name = get_first_name()
#	Set name_index = cipher(first_name)
#	Set calculated_passcode = generate_passcode(name_index)
#	Set input_passcode = input_passcode()
#	Set is_valid = is_passcode_integer(input_passcode)
#	Call module authenticate_passcode(is_valid, calculated_passcode)
#	Call module passcode_accepted()
# End Module

def main():
	first_name = "a"
	name_index = []
	# calculated_passcode = 0
	input_passcode = 0

	first_name = get_first_name()
	name_index = cipher(first_name)
	# calculated_passcode = generate_passcode(name_index)
	input_passcode = input_passcode_dialog()
#	authenticate_passcode(is_valied, input_passcode)
	authenticate_passcode(is_passcode_integer(input_passcode),generate_passcode(name_index))
	passcode_accepted()


# Call Module main()

main ()