#This is the tic tac toe game section
import random

# function: play_tic_tac_toe
def play_tic_tac_toe():
    # set player_score to 0
    player_score = 0
    # set round_counter to 1
    round_counter = 1 
    # while round_counter is less than or equal to 10
    while round_counter <= 10:
        # display message showing current round number
        print(f"You are on round {round_counter}/10.")
        # create empty tic tac toe board
        board_num = [[1,2,3],[4,5,6],[7,8,9]]
        board = [[" "," "," "],[" "," "," "],[" "," "," "]]
            # board should be 3x3 grid
            # each space starts empty
        # set current_player to "X" (user)
        current_player = "X"
        # game_over = False
        game_over = False
        # while game_over is False
        while game_over == False:
            # display current board

            print(f"{board[0][0]}|{board[0][1]}|{board[0][2]}\n"
                  f"_____\n"
                  f"{board[1][0]}|{board[1][1]}|{board[1][2]}\n"
                  f"_____\n"
                  f"{board[2][0]}|{board[2][1]}|{board[2][2]}\n")
            
            valid = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]


            # if current_player is "X"
            if current_player == "X":
                # ask user for row and column input
                row = int(input("Please input the row number of the positon you want to place here: "))
                column = int(input("Please input the column number of the positon you want to place here: "))
                # check if space is valid and empty
                    # if valid, place "X" in that space
                if [row-1,column-1] in valid and board[row-1][column-1] == " ":
                    board[row-1][column-1] = "X"
                    current_player = "O"
                    # if not valid, ask again
                else:
                    print("Invalid input or spot is taken. Choose again.")
                    continue
            # else if current_player is "O"
            elif current_player == "O":
                # generate computer move
                while True:
                    comp_row = random.randint(0,2)
                    comp_col = random.randint(0,2)
                    if board[comp_row][comp_col] != " ":
                        continue
                    else:
                        board[comp_row][comp_col] = "O"
                        current_player = "X"
                        break
                    # choose random empty space
                # place "O" in chosen space
            # check if current_player has won
            win = ""
            if board[0] == ["X","X","X"] or board[1] == ["X","X","X"] or board[2] == ["X","X","X"]:
                win = True
            elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
                win = True
            elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
                win = True
            elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
                win = True
            elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
                win = True
            elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
                win = True
            elif board[0] == ["O","O","O"] or board[1] == ["O","O","O"] or board[2] == ["O","O","O"]:
                win = False
            elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
                win = False
            elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
                win = False
            elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
                win = False
            elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
                win = False
            elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
                win = False
            elif board[0] != [" "," "," "] and board[1] != [" "," "," "] and board[2] != [" "," "," "]:
                win = False
            else:
                continue
                 # check rows
                # check columns
                # check diagonals
                # if win condition met
            if win == True:
                # add 1 to player_score
                player_score += 1
                # display winner message
                print("You WIN!")
                # set game_over to True
                game_over = True
            elif win == False:
                print("You lose.")
            
        
        # after round ends
        # add 1 to round_counter by 1
        round_counter += 1
    # after 10 rounds are complete
    if round_counter == 10:
    # display final score message
        # "You won X out of 10 rounds."
        print(f"You won {player_score}/10 rounds.")
    #return final score
    return player_score

play_tic_tac_toe()

