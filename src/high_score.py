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

#access csv function
def access_csv(game_name):
    # parameters: game_name
    # If the file does not exist, create it with a header row and return an empty dictionary

    # determine the correct CSV file path based on the game
    if game_name.lower() == "tic tac toe":
        path = "docs/tic_tac_toe.csv"
    elif game_name.lower() in ["number guess", "num guessing"]:
        path = "docs/num_guessing.csv"
    else:
        # if game name doesn't match expected games, just default to number guessing CSV
        path = "docs/num_guessing.csv"

    score_dict = {}  
    # empty dictionary to store all users and their scores

    try:
        # try to open the file in read mode
        with open(path, "r") as f:
            reader = csv.reader(f)
            next(reader, None)  
            # skip the header row (username, score_1, score_2, ...)
            # loop through each row in the CSV
            for line in reader:
                if not line:
                    continue  # skip empty lines
                username = line[0]  # first item is the username
                scores = []
                # convert the remaining items in the row to integers (the scores)
                for s in line[1:]:
                    try:
                        scores.append(int(s))
                    except ValueError:
                        continue  # skip any invalid score strings
                score_dict[username] = scores  # store in dictionary
    except FileNotFoundError:
        # if the file does not exist, create it with a header row
        with open(path, "w", newline="") as file:
            writer = csv.writer(file)
            # header row: username, score_1, score_2, ... score_10
            writer.writerow(["username"] + [f"score_{i+1}" for i in range(10)])
        score_dict = {}  # return empty dictionary because no data exists yet

    return score_dict  # return the dictionary of scores


# update high scores function
def update(new_score, score_dict, username):
    # parameters: new_score, score_dict, username
    scores = score_dict.get(username, [])  # get current scores for the user, or empty list if new user
    scores.append(new_score)  # add the new score
    scores.sort(reverse=True)  # sort scores from highest to lowest
    score_dict[username] = scores[:10]  # keep only top 10 scores
    return score_dict  # return updated dictionary


# --- Save dictionary back to CSV ---
def update_csv(score_dict, game_name):
    # parameters: score_dict, game_name
    if game_name.lower() == "tic tac toe":
        path = "docs/tic_tac_toe.csv"
    elif game_name.lower() in ["number guess", "num guessing"]:
        path = "docs/num_guessing.csv"
    else:
        path = "docs/num_guessing.csv"  # default

    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        # write header row
        writer.writerow(["username"] + [f"score_{i+1}" for i in range(10)])
        # loop through dictionary and write each user + their scores
        for user, scores in score_dict.items():
            row = [user] + scores
            writer.writerow(row)


# --- Format individual user scores ---
def format_individual(score_list, username):
    # parameters: score_list, username
    print(f"\nUsername: {username}")
    print("Personal Scores:")
    # enumerate allows us to loop through the list and also have a counter automatically
    for num, score in enumerate(sorted(score_list, reverse=True), start=1):
        print(f"{num}. {score}")  # display rank number and score


# --- Format top 5 overall scores ---
def format_overall(score_dict):
    # parameters: score_dict (dict)
    # purpose: display the top 5 scores from all users
    all_scores = []
    # gather all scores from all users into a single list
    for user, scores in score_dict.items():
        for s in scores:
            all_scores.append((user, s))  # store as tuple (username, score)

    # sort all scores from highest to lowest using the second item in the tuple (score)
    all_scores.sort(key=lambda x: x[1], reverse=True)

    print("Top 5 Overall Scores:")
    # show only the top 5 scores
    for num, (user, score) in enumerate(all_scores[:5], start=1):
        print(f"{num}. {user} -> {score}")


# --- Main high score workflow ---
def main_high(game_name, new_score, username):
    # parameters: game_name, new_score, username
    print(" Score Tracker:")
    scores = access_csv(game_name)  
    # get existing scores
    scores = update(new_score, scores, username)  
    # update scores with new score
    update_csv(scores, game_name)  
    # save updated scores back to CSV
    format_individual(scores.get(username, []), username) 
     # show individual scores
    format_overall(scores)  # show top 5 overall