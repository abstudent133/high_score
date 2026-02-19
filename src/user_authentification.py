# LV 1st User Authentification

# Requirements 

# - Find out if new or old user
# Ask user to enter username
# Store info as username
# Ask user to enter password
# Store info as password

# - Verify user logged in
# If username and password match
# Print "You've succesfully signed in"
# Exit loop (take them to the game)
# Else
# Print "Wrong username or password input"
# Print "Try again? (yes / no)"
# Store input as choice

# - All long information stored in separate file

# - Log out => Takes them to log in screen where they have the option to end program
# If choice is no
# Take them to main menu to EXIT
# Else take them back to sign in



# LD 1st User Sign up and Authentication

# Function that will be called if the user selects to sign up
# This function will ask the user for a username in a while loop
# Once a username has been typed in, open the csv for usernames and passwords
# Go through the csv and check if username the user gave is NOT equal to any already in there (this means that the user given username is unique and avaliable for use)
# Once user has a valid username, do a while loop for the password.
# See password requirements
# See helper function
# Once user has given both a valid username and password, put the given information into the csv (using hashlib for the password) and move onto selecting a game to play

# PASSWORD REQUIREMENTS
# length is >= 12
# Contains at least one number
# contains at least one UPPERCASE letter
# Contains at least one lowercase letter
# Contains at least one special character (maybe a tuple of all special characters that it compares to)

# HELPER FUNCTION
# this function will take in two parameters: the string it is checking for and which column (ex: pass in username and column 0 when checking if username avaliable and password + 1 for checking if password avliable)

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



# ISABELLA EXAMPLE. DELETE LATER
# if (20 >= 25 - 10 and 20 < 25) or (30 <= 25 + 10 and 20 > 25) <<< Example of if with numbers
# if (guess >= random_num - 10 and guess < random_num) or (guess <= random_num + 10 and guess > random_num)