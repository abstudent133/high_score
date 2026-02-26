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




# LD 1st User Sign up and Authentication
# \/ By LD
# Function that will be called if the user selects to sign up
# This function will ask the user for a username in a while loop
# Once a username has been typed in, open the csv for usernames and passwords
# Go through the csv and check if username the user gave is NOT equal to any already in there (this means that the user given username is unique and avaliable for use)
# Once user has a valid username, do a while loop for the password.
# See password requirements
# See helper function
# Once user has given both a valid username and password, put the given information into the csv (using hashlib for the password) and move onto selecting a game to play
def sign_up():
    def get_password():
        password = input("Enter the password you would like for your account:\n")
        return password
    while True:
        username = input("Enter the username you would like for your account:\n").strip()
        good_username = item_avaliable(username, 0)
        if good_username == True:
            # username was valid. Move onto password
            break
        else:
            print("It seems that the username you typed in is already taken. Enter a different username")
            continue
    while True:
        the_password = get_password()
        if pass_requirements(the_password) == True and item_avaliable(the_password, 1) == True:
            # password valid. add information
            break
        else:
            # Check which thing the password didn't meet and tell the user so
            print("Invalid pass")

# PASSWORD REQUIREMENTS
# length is >= 12
# Contains at least one number
# contains at least one UPPERCASE letter
# Contains at least one lowercase letter
# Contains at least one special character (maybe a tuple of all special characters that it compares to)
def pass_requirements(password):
    score = 0
    special_charcters = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "}", "[", "]", "|", "\\", ":", ";", '"', "'", "<", ">", ",", ".", "?", "/"]
    uppercase = any(char.isupper() for char in password)
    lowercase = any(char.islower() for char in password)
    digit = any(char.isdigit() for char in password)
    # Getting requirements
    if len(password) >= 12:
        score += 1
    if uppercase == True:
        score += 1
    if lowercase == True:
        score += 1
    if digit == True:
        score += 1
    for char in password:
        if char in special_charcters:
            score +=1 
            break
    # Requirments aquired. Now check if the score is a certain value. Return true if it is
    if score >= 5:
        return True
    else:
        return False
    

# HELPER FUNCTION
# this function will take in two parameters: the string it is checking for and which column (ex: pass in username and column 0 when checking if username avaliable and password + 1 for checking if password avliable)
def item_avaliable(string, column):
    # I need CSV to work on this
    # First, if column == 0, this is USERNAME
    # If column == 1, this is PASSWORD and I need to access the key to hash the given string BEFORE comparing
    # Open file first
    # If column == 0:
        # for line in content:
            # if string != line[0]
                # continue
            # else:
                # the username already made matches the given string. Not a valid username
                # return False
        # else:
            # This will run if loop did not break. If it did not break, username was unique
            # return True
    # elif column == 1:
        # for line in content:
            # the_key = line[2]
            # if string(that has been hashed by the_key) != line[1]
                # continue
            # else:
                # the password already made matches the given string. Not a valid password
                # return False
        # else:
            # This will run if loop did not break. If it did not break, password was unique
            # return True
    # else:
        # What in God's name did you do to my code?!?!?!?!? Column should only be 1 or 2
    pass

# ADMIN FUNCTIONALITY
# Information is already established when csv is created
# This option will be displayed on sign in menu
# FUNCTION
# This will take in user input of username
# Check if username == admin username in csv
# Check samething with password
# IF both username and password match, allow user acess to add or remove a user
# IF ADD USER
# See if I can just call the sign up function
# IF REMOVE USER
# Ask for username and password corresponding to user they want to remove
# See LD's personal library to usnderstand how to remove row from csv
    # IN SHORT: open two files, one in and one out. In is original and is refereance point for what to keep and what to delete. If item something to KEEP, write it onto out file. If item is what we want DELETED, don't write it to outfile. Once that's done, use os to delete infile and use os to rename outfile to match original infile name (that way code doesn't break because we aren't trying to reference different file names)
def admin():
    username = input("Enter the Admin Username:\n").strip()
    valid_usrnm = item_avaliable(username, 0)
    if valid_usrnm != True:
        # Username MATCHES, this what I want. Now do password
        pass
    else:
        print("Invalid username. Returning to Sign In Menu . . .")
        # Go to that function? or it's in a while loop and thus return
    password = input("Enter the Admin Password:\n").strip()
    valid_pass = item_avaliable(password, 1)
    if valid_pass != True:
        # Password MATCHES, that what I want.
        pass
    else:
        print("Invalid password. Returning to Sign In Menu . . .")
        # Go to that function? or it's in a while loop and thus return
    # IN THEORY the username and password are valid and now need to do the special admin capabilities
    while True:
        print("What would you like to do:\n1) Add a User\n2) Remove a User\n3) Go Back to Sign In Menu")
        action = input("Enter the number corresponding to what you want to do:\n")
        if action == "1":
            # Call sign up function because LAZY
            pass
        elif action == "2":
            # Oh boy.... I dont want to do this. See LD's personal library
            pass
        elif action == "3":
            print("Returning to Sign In Menu . . .")
        else:
            print("Invalid input. Please try again")
            continue