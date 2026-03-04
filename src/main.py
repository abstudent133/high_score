#This is the main for the user interface

# SIGN IN MENU
# get user to sign in / sign up / log in as admin / leave program entirly

# \/ By LV
# - Log out => Takes them to log in screen where they have the option to end program
# If choice is no (not sign in)
# End the code
# Else take them back to sign in
from guessing_gme import guessing_game
# \/ By IC
# MENU FOR SIGNED IN
print("tick tack toe = 1, guessing game = 2, view high score = 3 log out = 4")
# tick tack toe option is 1 
# guessing game is 2
# view high score is 3 
# log out is 4 
#  if user choice is 1
user_choice = input("please choose one of those numbers: ")
if user_choice == "1":
#      then play the function for number guessing game
        guessing_game()
#   # else if user choice is 2
#       then play the tick tac toe function 
#   # else if user choice is 3 
        #play the high score function 
      #  if user choice is 4
        #then have them log out and sent to main menu for sign in and such 
#   else:
        #show the user incorrect input try again
        #send the user back up 
        