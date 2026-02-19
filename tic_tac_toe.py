#This is the tic tac toe game section

# function: play_tic_tac_toe
# set player_score to 0
# set round_counter to 1
# while round_counter is less than or equal to 10
    # display message showing current round number
    # create empty tic tac toe board
        # board should be 3x3 grid
        # each space starts empty
    # set current_player to "X" (user)
    # game_over = False
    # while game_over is False
        # display current board
        # if current_player is "X"
            # ask user for row and column input
            # check if space is valid and empty
                # if valid, place "X" in that space
                # if not valid, ask again
        # else if current_player is "O"
            # generate computer move
                # choose random empty space
            # place "O" in chosen space
        # check if current_player has won
            # check rows
            # check columns
            # check diagonals
            # if win condition met
                # if current_player is "X"
                    # add 1 to player_score
                # display winner message
                # set game_over to True
        # else check if board is full (tie)
            # if tie
                # display tie message
                # set game_over to True
        # if game not over
            # switch current_player
                # if "X" change to "O"
                # if "O" change to "X"
    # after round ends
    # add 1 to round_counter by 1
# after 10 rounds are complete
# display final score message
    # "You won X out of 10 rounds."
#return final score

