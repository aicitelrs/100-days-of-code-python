print('''
*******************************************************************************
          |                   |                  |                     |
 _________|______    action_choice = input(
        "After walking a few steps, you came across a river. Choose between swimming or waiting. Type 'swim' or 'wait'.\n"
    ).lower()__________.=""_;=.______________|_____________________|_______
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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
path_choice = input("You've walked into a cave and you see two paths. One to the left and one to the right. Type one of those.\n").lower()
if path_choice == "left":
    action_choice = input("After walking a few steps, you came across a river. Choose between swimming or waiting. Type 'swim' or 'wait'.\n").lower()
    if action_choice == "wait":
          door_choice = input("You waited for a while, and a boat came to pick you up. You got on the boat and arrived at the other side of the river. You see three different-colored doors in the distance (red, yellow, blue) and you have to choose one. Type 'red', 'yellow' or 'blue'.\n").lower()
          if door_choice == 'yellow':
              print("You found the treasure! Congratulations!")
          elif door_choice == 'blue':
              print("You got eaten by beasts. Game over!")
          elif door_choice == 'red':
              print("Sorry! You got burned by fire. Game over!")
          else:
              print("Game over!")          
    else:
          print("You got attacked by a trout. Game over!")

else:
    print("You fell into a hole. Game Over.")
