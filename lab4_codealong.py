__author__ = "voidfemme"

# Code-along with Lab4 video in CIS 122

# Function Boolean is_valid_integer (String input_string)
#	Declare Boolean is_valid
#
#
# 	is_valid = is input_string a valid integer?
#	Return is_valid
# End function

def is_valid_integer(input_string):
	try:
		int(input_string)
		is_valid = True
	except ValueError:
		is_valid = False
	return is_valid

# Function integer get_number_of_fibonacci_numbers()
#	Declare String input_string
#	Declare Boolean is_valid
#	Display "How many Fibonacci number do you want? "
#	Input input_string
#	Set is_valid = is_valid_integer(input_string)
#	While Not is_valid
#		Display "Please enter a whole number! "
#		Input input_string
#		Set is_valid = is_valid_integer(input_string)
#	End While
#	input_integer = int(input_string)
# Return input_integer
# End function

def get_number_of_fibonacci_numbers():
	input_string = input("How many fibonacci numbers do you want? ")
	is_valid = is_valid_integer(input_string)
	while not is_valid:
		input_string = input("Please enter a whole number. ")
		is_valid = is_valid_integer(input_string)
	input_integer = int(input_string)
	return input_integer

# Module output_fibonacci(Integer counter, Integer first, Integer second, Integer next)
#	Display "Fibonacci number", counter, "is", first, "+", second, "=", next
# End module

def output_fibonacci(counter, first, second, next):
	print("Fibonacci number", counter, "is", first, "+", second, "=", next)

# Module calculate_fibonacci(Integer n)
# 	Declare Integer first = 1
# 	Declare Integer second = 1
#	Declare Integer counter = 0
#	Declare Integer next
#	Set counter = 0
# 	While counter < n
# 		next = first + second
#		counter = counter + 1
#		Call output_fibonacci(first, second, next)
#		first = second
#		second = next
#	End While

def calculate_fibonacci(n):
	first = 1
	second = 1
	counter = 0
	if(n<1):
		return
	print("Fibonacci number 1 is 1")
	if(n<2):
		return
	print("Fibonacci number 2 is 1")
	while counter < n - 2:
		next = first + second
		counter = counter + 1
		output_fibonacci(2 + counter, first, second, next)
		first = second
		second = next


# Module calculate_fibonacci_sequence()
#	Set n = get_number_of_fibonacci_numbers()
#	Call calculate_fibonacci(n)
# End Module

def calculate_fibonacci_sequence():
	n = get_number_of_fibonacci_numbers()
	calculate_fibonacci(n)

calculate_fibonacci_sequence()