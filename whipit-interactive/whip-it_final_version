__author__="Rose S Proctor"
# Does DEVO Think You Should "Crack That Whip," Or "Move Ahead?"
# This program is designed to determine if DEVO thinks you should "crack that whip" or "move ahead," as indicated by their 1980's hit, "Whip It."

# When a problem comes along
# You must whip it
# Before the cream sits out too long
# You must whip it
# When something's going wrong
# You must whip it
# Now whip it
# Into shape
# Shape it up
# Get straight
# Go forward
# Move ahead
# Try to detect it
# It's not too late
# To whip it
# Whip it good
# When a good time turns around
# You must whip it
# You will never live it down
# Unless you whip it
# No one gets away
# Until they whip it
# I say whip it
# Whip it good
# I say whip it
# Whip it good
# Crack that whip

# Define module main()
#   Display "Does DEVO Think You Should "Crack That Whip," Or "Move Ahead?" Let's find out!"
#   Call module problem()

# Define module problem()
#   If "Has a problem come along?" == y, Then
#     Call module whip_it("you must")
#   Else
#     Call module cream()

# Define module cream()
#   If "Has the cream sat out too long??" == y, Then
#     Call module whip_it("you must")
#   Else
#     Call module wrong()

# Define module wrong()
#   If "Is something going wrong?" == y, Then
#   Call module whip_it("you must")
#   Else
#     Call module good_time()

# Define module good_time()
#   If "Has a good time turned around??" == y, Then
#   Call module whip_it("you must")
#   Else
#     Call module lived_down()

# Define module lived_down()
#   If "Have you ever lived it down?" == y, Then
#   Call module whip_it("not unless you")
#   Else
#     Call module gotten_away()

# Define module gotten_away()
#   If "Has anyone gotten away?" == y, Then
#   Call module whip_it("not until they")
#   Else
#     Call module crack_that_whip()

# Define Module whip_it("string")
#   Display: string," whip it!"
#   Call module whipped_good()

# Define module whipped_good()
#   If "Is it whipped good" == y Then
#     Display "you should move ahead"
#   else
#     Call module crack_that_whip()


# Define module crack_that_whip()
#   Display "you should crack that whip"

# Call module main()

#########################################################################3

def main():
  print("Does DEVO Think You Should \"Crack That Whip,\" Or \"Move Ahead?\" Let's find out!")
  print("type \"yes\" or \"no\"")
  problem()

def problem():
  it_has = ""
  yes = "yes"
  it_has = input("Has a problem come along? ")
  if it_has == yes:
    whip_it("you must")
  else:
    cream()

def cream():
  it_has = ""
  yes = "yes"
  it_has = input("Has the cream sat out too long? ")
  if it_has == yes:
    whip_it("you must")
  else:
    wrong()

def wrong():
  it_has = ""
  yes = "yes"
  it_has = input("Is something going wrong? ")
  if it_has == yes:
    whip_it("you must")
  else:
    good_time()

def good_time():
  it_has = ""
  yes = "yes"
  it_has = input("Has a good time turned around? ")
  if it_has == yes:
    whip_it("you must")
  else:
    lived_down()

def lived_down():
  you_have = ""
  yes = "yes"
  you_have = input("Have you ever lived it down? ")
  if you_have == yes:
    whip_it("not unless you")
  else:
    gotten_away()

def gotten_away():
  it_has = ""
  yes = "yes"
  it_has = input("Has anyone gotten away? ")
  if it_has == yes:
    whip_it("you must")
  else:
    crack_that_whip()

def whip_it(string):
  print(string,"WHIP IT!")
  whipped_good()
  
def whipped_good():
  it_is = ""
  yes = "yes"

  it_is = input("... is it whipped good? ")
  if it_is == yes:
    print("DEVO thinks you should move ahead")
  else:
    crack_that_whip()

def crack_that_whip():
  print(" DEVO thinks you should crack that whip")

main()
