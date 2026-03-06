#This is the main for the user interface
from guessing_gme import *
from high_score import *
from tic_tac_toe import *
from user_authentification import *

# SIGN IN MENU
# get user to sign in / sign up / log in as admin / leave program entirly

# \/ By LV
# - Log out => Takes them to log in screen where they have the option to end program
# If choice is no (not sign in)
# End the code
# Else take them back to sign in
# Otions for sign in menu
def display_menu():
    print("1. Sign in")
    print("2. Sign up")
    print("3. Admin sign in")
    print("4. Exit") 

# Main menu
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            sign_in()
            signed_in_menu()
        elif choice == "2":
            sign_up()
            signed_in_menu()
        elif choice == "3":
            # admin() # Change name once the function is made
            print("Admin functionality unavaiable as of this moment. Pick something else")
            continue
        elif choice == "4":
            print("Thank you for using High Score! Goodbye!")
            exit()
        else:
            print("Please enter a valid choice (1, 2, 3, or 4)")
            # Return to main menu

# \/ By IC
# MENU FOR SIGNED IN
def signed_in_menu():
    while True:
        print("Tick tack toe = 1,")
        print("Guessing game = 2,")
        print("View high score = 3")
        print("Log out = 4")
                # tick tack toe option is 1 
                # guessing game is 2
                # view high score is 3 
                # log out is 4 
                #  if user choice is 1
        user_choice = input("Please choose one of those numbers: ").strip()
        if user_choice == "1":
                #      then play the function for number guessing game
            play_tic_tac_toe()
                #   # else if user choice is 2
        elif user_choice == "2":
                #       then play the tick tac toe function 
            guessing_game()
                #   # else if user choice is 3 
        elif user_choice == "3":
            username = input("Please input your username again here: ")
            print("Tic Tac Toe High Scores:")
            main_high("tic tac toe", 0, username)   # 0 = no new score
            print("Number Guessing Game High Scores:")
            main_high("number guess", 0, username)
        elif user_choice == "4":
                        #then have them log out and sent to main menu for sign in and such 
            main()
                #   else:
        else:
                        #show the user incorrect input try again
                        #send the user back up 
            print("Invalid choice. Try again")
            continue
main()