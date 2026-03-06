# \/ By AB
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
import csv

#access csv
def access_csv(game_name):
# parameters: game_name
    # determine which game file should be opened
    # create empty dictionary called score_dictionary
    score_dictionary = {}
    # open the selected csv file
    with open(game_name, mode="r") as csv_file:
        content = csv.reader(csv_file)
        # for each row in the csv file
        for line in content:
            # first value should be the user id (key)
            # remaining values should be the list of top 5 scores
            # convert score values from string to integer
            username = line[0]
            scores = []
            for score in line[1:]:
                scores.append(int(score))
            score_dictionary[username] = scores
        # close the file
        # return score_dictionary
        return score_dictionary

#update high scores function
def update(new_score, score_dictionary, username,):
# parameters: new_score, score_dictionary, username
        # search dictionary for username as key
    scores = score_dictionary.get(username, [])
    # check if new_score is greater than the lowest score in the list
    scores.append(new_score)
    # if it is greater
            # add new_score to the list
            # sort the list from highest to lowest
            # remove the lowest score so only top ten remain
    # update dictionary with modified score list
    for score in scores:
        if new_score >= score:
            if new_score == score[0]:
                continue
            else:
                scores.append(new_score)
                scores = scores.sort()
                score.remove(scores[0])
                score_dictionary[username] = scores
        else:
            continue
    # return updated dictionary
    return score_dictionary

# update csv function
def update_csv(dictionary, game_name):
# parameters: updated_dictionary, game_name
    # determine which csv file to open based on game_name
    if game_name == "tic tac toe":
        file_name = "docs/tic_tac_toe.csv"
    elif game_name == "number guess":
        file_name = "docs/number_guess.csv"
    # open the file in write mode (this will overwrite old data)
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
    # for each key and score list in updated_dictionary
        for key, scores in dictionary.items():
        # write a row to the csv
            row = [key] + scores
            writer.writerow(row)
            # first value = user id
            # remaining values = top ten scores
    # close the file

# formate individual function
def formate_individual(score_list, username):
# parameters: score_list, username
    # display header that includes the username
    print(f"Username: {username}")
    # sort score_list from highest to lowest
    num = 0
    score_list = score_list.sort()
    print("Scores:")
    # loop through scores
    for score in score_list:
        # display rank number and score
        print(f"{num}. {score}")
        num += 1
        
   
#formate overall funtion
def formate_overall(dictionary):
#parameters: dictionary
    all_scores = []
# gather all scores from dictionary
    for username, scores in dictionary.items():
        for score in scores:
            all_scores.append((username, score))
# sort from highest to lowest
    all_scores.sort(key=lambda x: x[1])
    print("Top 5 Overall Scores:")
# take top five
    for i in range(5):
        username, score = all_scores[i]
# display username associated with each score
        print(f"{i+1}. {username} -> {score}")

#main
def main_high(game,new_score,username):
    print("This is the high score tracker.")
    if game == "tic tac toe":
        score_dictionary = access_csv("tic tac toe")
        score_dictionary = update(new_score,score_dictionary,username,"personal")
        score_dictionary = update(new_score,score_dictionary,username,"overall")
        update_csv(score_dictionary,"tic tac toe")
        formate_individual(score_dictionary.get(username),username)
        formate_overall(score_dictionary)
    else:
        score_dictionary = access_csv("number guess")
        score_dictionary = update(new_score,score_dictionary,username,"personal")
        score_dictionary = update(new_score,score_dictionary,username,"overall")
        update_csv(score_dictionary,"number guess")
        formate_individual(score_dictionary.get(username),username)
        formate_overall(score_dictionary)
        




