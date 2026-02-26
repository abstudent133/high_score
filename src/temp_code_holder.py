# File to hold code being worked on so that there aren't merge issues

# LV 1st User Authentification
import csv

# Requirements 

# - Find out if new or old user
# Ask user to enter username
# Store info as username
# Ask user to enter password
# Store info as password

# - Verify user logged in
# If username and password match
# Print "You've succesfully signed in"
# Exit loop (take them to the game/signed in menu)
# Else
# Print "Wrong username or password input"
# Print "Try again? (yes / no)"
# Store input as choice

def sign_in():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        # Open csv and check if username and password match
        csv_file = open("user_info.csv", "r") # going to change the name of the csv file once we have it
        csv_reader = csv.reader(csv_file)
        match = False
        for row in csv_reader:
            if row[0] == username and row[1] == password:
                match = True
                break
        csv_file.close()
        # If they do, print "You've succesfully signed in" and break loop
        if match:
            print("You've succesfully signed in")
            break
        # Else, print "Wrong username or password input" and ask "Try again? (yes / no)"
        # Store input as choice
        else:
            print("Wrong username or password input")
            choice = input("Try again? (yes / no): ")
        # If choice is no, exit program
        if choice == "no":
            exit() # main() or exit()
        # Else, continue loop to try again
        else:
            continue
# Test code later once I have the CSV file

# - All long information stored in separate file