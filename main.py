print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 




directions = (input("You're ate a cross road. Where do you want to go?\nType 'left' or 'right'. ")).lower()
if directions == "right":
  print("Fall into a hole.\nGame over!")
elif directions == "left":
    directions = (input("You come to a lake. There is an island in the middle of the lake.\nType 'wait' to wait for a boat. Type 'swim' to swim across. ")).lower()
    if directions == "swim":
      print("You were attacked by a trout.\nGame over!")
    elif directions == "wait":
      directions = (input("You arrive at the island unharmed.\nThere is a house with three doors.\nOne red, one blue and one yellow.\nWich color do you choose? ")).lower()
      if directions == "red":
        print("You were burned by fire.\nGame over!")
      elif directions == "blue":
        print("You were eanten by beasts.\nGame over!")
      elif directions == "yellow":
        print("You found the treasure.\nYou Win!")
      else:
        print("You chose a door that doesn't exist.\nGame over!")
    else:
      print("You got attacked by an angry trout.\nGame over!")
else:
  print("You fell into a hole!\nGame over!")
