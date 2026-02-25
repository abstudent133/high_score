# File to hold code being worked on so that there aren't merge issues

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
    

# Go through the csv and check if username the user gave is NOT equal to any already in there (this means that the user given username is unique and avaliable for use)
# Once user has a valid username, do a while loop for the password.
# this function will take in two parameters: the string it is checking for and which column (ex: pass in username and column 0 when checking if username avaliable and password + 1 for checking if password avliable)
def item_avaliable(string, column, key):
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
                # break
    # elif column == 1:
        # for line in content:
            # the_key = line[2]
            # if string(that has been hased by the_key) != line[1]
                # continue
            # else:
                # the password already made matches the given string. Not a valid password
                # break
    # else:
        # What in God's name did you do to my code?!?!?!?!? Column should only be 1 or 2
    pass