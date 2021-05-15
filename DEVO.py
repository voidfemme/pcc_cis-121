def main():
  print("Does DEVO think You \"give the past a slip,\"  or that you \"break your mother\'s back?\" Let's find out!")
  print("type \"yes\" or \"no\"")
  crack_that_whip()
  
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
    whip_it("You must")
  else:
    wrong()

def wrong():
  it_has = ""
  yes = "yes"
  it_has = input("Is something going wrong? ")
  if it_has == yes:
    whip_it("You must")
  else:
    good_time()

def good_time():
  it_has = ""
  yes = "yes"
  it_has = input("Has a good time turned around? ")
  if it_has == yes:
    whip_it("You must")
  else:
    lived_down()

def lived_down():
  you_have = ""
  no = "no"
  you_have = input("Have you ever lived it down? ")
  if you_have == no:
    whip_it("Not unless you")
  else:
    gotten_away()

def gotten_away():
  it_has = ""
  no = "no"
  it_has = input("Has anyone gotten away? ")
  if it_has == no:
    whip_it("Not until they")
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
    in_shape()
  else:
    whip_it("you must")

def in_shape():
  it_is = ""
  yes = "yes"
  it_is = input("... is it in shape? ")
  if it_is == yes:
    crack_that_whip()
  else:
    shape_up()

def shape_up():
  i_did = ""
  yes = "yes"
  i_did = input("... will you shape it up? ")
  if i_did == yes:
    crack_that_whip()
  else:
    get_straight()

def get_straight():
  it_is = ""
  yes = "yes"
  it_is = input("... will you get it straight? ")
  if it_is == yes:
    crack_that_whip()
  else:
    go_forward()

def go_forward():
  it_will = ""
  yes = "yes"
  it_will = input("... will it go forward? ")
  if it_will == yes:
    crack_that_whip()
  else:
    move_ahead()

def move_ahead():
  i_did = ""
  yes = "yes"
  i_did = input("... did you move ahead? ")
  if i_did == yes:
    crack_that_whip()
  else:
    detect_it()

def detect_it():
  i_did = ""
  yes = "yes"
  i_did = input("... did you detect it? ")
  if i_did == yes:
    crack_that_whip()
  else:
    whip_it("it\'s not too late to")

def crack_that_whip():
  i_did = ""
  yes = "yes"
  i_did = input("Did you crack that whip!? ")
  if i_did == yes:
    print("DEVO says you gave the past a slip!")
  else:
    step_on_crack()

def step_on_crack():
  i_did = ""
  yes = "yes"
  i_did = input("Did you step on a crack? ")
  if i_did == yes:
    print("DEVO says you break your mama\'s back!")
  else:
    problem()

main()
