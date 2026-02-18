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

#access_csv function
#parameters are (tic_or_num)
    #open the high_