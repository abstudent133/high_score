# LV 1st User Authentification
import csv
import hashlib
import os

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
        csv_file = open("docs/user_login.csv", "r") # going to change the name of the csv file once we have it   # Note from LD: You can't just have password be compared, it needs to be hashed first (I built a helper function for this, feel free to use it. Just pass in the string you need hashed)
        match = True
        csv_reader = csv.DictReader(csv_file)
        match = False
        for row in csv_reader:
            encoded_string = password.encode('utf-8')
            hasher = hashlib.sha256()
            hasher.update(encoded_string)
            final_hash = hasher.hexdigest()
            if row['username'] == username and row['password'] == final_hash:
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
    while True:
        the_username = input("Enter the username you would like:\n").strip()
        user_avaliable = item_avaliable(the_username, 0)
        if user_avaliable == True:
            # Valid username, go to password
            break
        else:
            print("It seems that username is already taken. Please input a different username")
            continue
    while True:
        the_password = input("Enter the password you would like\nPassword must be 12 characters long (maximum is 40), have a number, have an uppercase, have a lowercase, and have a special character:\n").strip()
        pass_valid = pass_requirements(the_password)
        if pass_valid == True:
            # password meets requirements. Now check if password avaliable
            pass
        else:
            print("Your password doesn't have the nessisary requirements. Please enter a different password")
            continue
        pass_avaliable = item_avaliable(the_password, 1)
        if pass_avaliable == True:
            # password avaliable and meets requirements. add info to csv
            break
        else:
            print("It seems that the password you typed has already been taken. Please enter a different password")
            continue
    # Enter aquired information to csv
    hashed_pass, the_key = hash_item(the_password)
    with open("docs/user_login.csv", "a", newline="") as csv_file:
        fieldnames = ['username', 'password', 'key']
        writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
        writer.writerow({'username': the_username, 'password': hashed_pass, 'key': the_key})

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
    if len(password) >= 1 and len(password) <= 40:
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
    avaliable = True
    csv_file = open("docs/user_login.csv", 'r', newline='')
    csv_reader = csv.DictReader(csv_file)
    if column == 0:
        for line in csv_reader:
            if string == line['username']:
                avaliable = False # found a match meaning item is not unique
                break
            else:
                continue
    elif column == 1:
        for line in csv_reader:
            # First hash the string (password) with the key in the line
            encoded_string = string.encode('utf-8')
            hasher = hashlib.sha256()
            hasher.update(encoded_string)
            final_hash = hasher.hexdigest()
            if final_hash == line['password']:
                # Found a match. Invalid
                avaliable = False
                break
            else:
                continue
    else:
        print("What the hell?")  
    return avaliable 

def hash_item(hash_item):
    encoded_string = hash_item.encode('utf-8')
    hash_object = hashlib.sha256()
    hash_object.update(encoded_string)
    hex_hash = hash_object.hexdigest()

    #random_hasher = random.choice(keys_to_use)
    #byte_item = hash_item.encode(random_hasher)
    #hash_object = hashlib.sha256(byte_item)
    #final_hashed = hash_object.hexdigest()
    return hex_hash, 'sha256()'

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
    if valid_usrnm == False:
        # Username MATCHES, this what I want. Now do password
        pass
    else:
        print("Invalid username. Returning to Sign In Menu . . .")
        # Go to that function? or it's in a while loop and thus return
        exit()
    password = input("Enter the Admin Password:\n").strip()
    valid_pass = item_avaliable(password, 1)
    if valid_pass == False:
        # Password MATCHES, that what I want.
        pass
    else:
        print("Invalid password. Returning to Sign In Menu . . .")
        # Go to that function? or it's in a while loop and thus return
        exit()
    # IN THEORY the username and password are valid and now need to do the special admin capabilities
    while True:
        print("What would you like to do:\n1) Add a User\n2) Remove a User\n3) Go Back to Sign In Menu")
        action = input("Enter the number corresponding to what you want to do:\n")
        if action == "1":
            # Call sign up function because LAZY
            sign_up()
        elif action == "2":
            # Oh boy.... I dont want to do this. See LD's personal library
            remove_usrnm = input("Enter the username you would like to remove:\n").strip()
            temp_filename = "temp_user_info.csv"
            with open("docs/user_login.csv", mode='r', newline='') as infile, open(temp_filename, mode='a', newline='') as outfile:
                reader = csv.DictReader(infile)
                fieldnames = ['username', 'password', 'key']
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()

                for row in reader:
                    if row['username'] == remove_usrnm:
                        # Found the username we want gone. Do nothing so that it isn't writen to the outfile
                        continue
                    else:
                        writer.writerow(row)
            os.remove("docs/user_login.csv")
            os.rename(temp_filename, "docs/user_login.csv")
        elif action == "3":
            print("Returning to Sign In Menu . . .")
        else:
            print("Invalid input. Please try again")
            continue