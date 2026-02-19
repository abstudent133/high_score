#This is the pseudocode and code for the high score tracking part of this project
#personal project analysis

#Access csv function
#need to know if it is the tic tac toe or num guessing
#actions:
    #open the csv for the correct game
    #transform it into a dictionary 
    #return that dictionary

#Interperet Dictionary list function
#parameters are the new high score and the dictionary and the username and if it is the overall for personal
#actions:
    #if personal
        #search for the user by key
    #if general
        #search for key overall
    #check all of the scores against the current high scores
    #add if it is greater than the one
    #delete the lowest value in the list
    #return the updated dictionary

#formate and display function
#paremeters are the list of values the username
#actions
    #formate the username and the top ten scores
    #display those scores

#update csv funciton
#parameters are this dictionary
#actions:
    #open the correct csv
        #for each line in the dictionary 
                #write it in the csv
#Pseudocode
#import csv

#access csv
# parameters: game_name
# determine which game file should be opened
# if game_name is "tic_tac_toe"
    # set file_name to tic_tac_toe_high_scores.csv
# else if game_name is "number_guess"
    # set file_name to number_guess_high_scores.csv
# open the selected csv file
# create empty dictionary called score_dictionary
# for each row in the csv file
    # first value should be the user id (key)
    # remaining values should be the list of top ten scores
    # convert score values from string to integer
    # store in dictionary as:
        # key = user id
        # value = list of scores
# close the file
# return score_dictionary

#update high scores function
# parameters: new_score, score_dictionary, username, score_type
# if score_type is "personal"
    # search dictionary for username as key
# else if score_type is "overall"
    # search dictionary for key "overall"
# get the score list for that key
# check if new_score is greater than the lowest score in the list
    # if it is greater
        # add new_score to the list
        # sort the list from highest to lowest
        # remove the lowest score so only top ten remain
# update dictionary with modified score list
# return updated dictionary

# update csv function
# parameters: updated_dictionary, game_name
# determine which csv file to open based on game_name
# open the file in write mode (this will overwrite old data)
# for each key and score list in updated_dictionary
    # write a row to the csv
        # first value = user id
        # remaining values = top ten scores
# close the file

# formate individual function
# parameters: score_list, username
# display header that includes the username
# sort score_list from highest to lowest
# loop through scores
    # display rank number and score
   
#formate overall funtion
#parameters: dictionary
# gather all scores from dictionary
# sort from highest to lowest
# take top five
# display username associated with each score