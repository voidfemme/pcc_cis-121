# prompt the user to enter product model number
#	only accept the values 100, 200, 300


# Function Boolean gemma(Integer model)
#	Declare Boolean status
#	If model != 100 AND model != 200 AND model != 300 Then
#		Set status = True
#	Else
#		Set status = False
#	End If
#	Return status
# End Function

# Function Integer alex(String prompt)
#	Declare Integer num
#	While True
#		Try
#       	Display prompt
#       	Input num
#       	Break
#		Except
#       	Display "Not an integer" 
#	End While
# 	Return num
# End Function

# Function Integer ell()
# 	Declare Integer model
# 	Set model = alex("Enter a valid model number") 
# 	While gemma(model)
#   	Display "The valid model numbers are 100, 200, and 300."
#   	Set model = alex("Enter a valid model number")
# 	End While
# 	Return model
# End Function

# Module rose()
#     Declare Integer modelNum
#     modelNum = ell()
#     Display “You entered model number: “, modelNum
# End Module

# gemma gets the number ell gives her and compares
# it to her list of favorite numbers. Her favorite 
# numbers are 100, 200, and 300!

def gemma(model):
	print("Gemma decides whether", model, "is one of her favorite numbers...")
	print("")
	status = False
	model = int(model)
	if model == 100 or model == 200 or model == 300:
		status = False
		print("Gemma tells ell that",model, "is one of my favorites! (^_^)")
		print("")
	else:
		status = True
		print("Gemma tells ell that",model,"is NOT one of my favorites. '>_<'")
		print("")
	return status

# when alex gets the paper from ell, they then
# write down what make sure it is an integer. 
# if it is an integer, they give the paper back 
# to ell. if it isn't, they try again until it is.

def alex():
	num = input(">>> Alex guesses one of Gemma's favorite numbers: ")
	print("")
	while True:
		try:
			int(num)
			print("Alex writes", num,"on ell's piece of paper")
			print("")
			break
		except:
			num = input(">>> Alex needs an integer, try again: ")
			print("")
	return num

# ell gives that piece of paper that rose 
# gave her and gives it to alex to write on,
# with some instructions. when ell gets that 
# paper back, she then gives that paper to 
# gemma and asks gemma if the model matches 
# one of her favorite numbers.

def ell():
	model = int
	print("ell asks alex to pick a number")
	print("")
	model = alex()
	print("ell checks to see if",model,"is one of Gemma's favorites.")
	print("")
	while gemma(model):
		print("ell informs Alex that Gemma's favorite numbers are the first three multiples of 100.)")
		print("")
		model = alex()
	return int(model)

# Rose wants to know what Gemma's favorite 
# numbers are, so she gives ell a piece of
# paper to write down what Gemma's favorite
# numbers are. When rose gets that peice
# of paper back, she reads what it says.

def rose():
	print("Rose asks ell to find out what Gemma's favorite numbers are")
	print("")
	modelNum = int
	modelNum = ell()
	print("Rose discovered that", modelNum, "is one of Gemma's favorites.")
	print("")

rose()