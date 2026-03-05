#IC 1st guessing number game 
#import random 
import random
from high_score import*
#definging score
def guessing_game():
    score = 0
    # show the user hello you have entered the numbers guessing game 
    print("Hello you have entered the numbers guessing game!")
    # the point of this game is to guess a number between 1 - 500
    print("The point of this game is to guess a number between 1- 200")
    # quit is equal to false 
    quit = False
    # while quit is equal to false let the game contiune 
    while quit == False: 
    #   get a random number in the range of 1 - 500
        random_number = random.randint(1,201)
    #   show the user im thinking abt a number from 1 - 500 how abt you guess
        print("Im thinking about a number from 1 - 200")
    #   asking the user guess a number bewtween 1 - 500 
        guess_input = input("Guess a number between 1-200:").strip()
        if int(guess_input) == False:
            guess_input = input("guess a number between 1-200:")
        if guess_input.isdigit() == False:
            print("Enter a number please")
            continue
    #   save this as a variable under the name guess 
        guess = int(guess_input)
        if guess > 200 or guess < 1:
            print("That is a number out of the given range. Please input a number between 1 and 200")
            continue
        if guess == random_number:
            score += 10
            print(f"Your score is {score}!")
    #       # if (guess >= random_num - 10 and guess < random_num) or (guess <= random_num + 10 and guess > random_num)
                #add seven to the score 
            print(f"The random number was {random_number}")
        elif (guess >= random_number - 10 and guess < random_number) or (guess <= random_number + 10 and guess > random_number):
                #add seven to the score 
                score += 7 
                print(f"Your score is {score}")
                print(f"The random number was {random_number}")
            # if (guess >= random_num - 20 and guess < random_num) or (guess <= random_num + 20 and guess > random_num)
        elif (guess >= random_number - 20 and guess < random_number) or (guess <= random_number + 20 and guess > random_number):
            #add five to score
            score += 5 
            print(f"Your score is {score}")
            print(f"The random number was {random_number}")
            # if (guess >= random_number - 30 and guess < random_number) or (guess <= random_number + 30 and guess > random_number)
        elif (guess >= random_number - 30 and guess < random_number) or (guess <= random_number + 30 and guess > random_number):
    #         # add three to score
            score += 3
            print(f"Your score is {score}")
            print(f"The random number was {random_number}")
            # if (guess >= random_num - 40 and guess < random_num) or (guess <= random_num + 40 and guess > random_num)
        elif (guess >= random_number - 40 and guess < random_number) or (guess <= random_number + 40 and guess > random_number):
                # add two to score
            score += 2
            # if (guess >= random_num - 50 and guess < random_num) or (guess <= random_num + 50 and guess > random_num)
            print(f"Your score is {score}")
            print(f"The random number was {random_number}")
        elif (guess >= random_number - 50 and guess < random_number) or (guess <= random_number + 50 and guess > random_number):
                # add one to score
            score += 1
            print(f"Your score is {score}")
            print(f"The random number was {random_number}")
            #else:
        else:
                #show the user you got no points
            print(f"Your score is {score}")
            print(f"The random number was {random_number}")
           
            print("You got no points")
        # ask user if they want to play again (yes/no)
        again = input("Do you want to play again yes or no:").strip().lower()
            # if yes
        if again == "yes":
                        # quit equals true
            quit = False
                    
            continue
                    # else:
        elif again == "no":
            print("goodbye")
            quit = True
            username = input("Please input your username here: ")
            main_high("number guess",score, username)
            break
        else:
            print("incorrect input")
    
    return score

    # at end, send back to signed in menu   
    quit == True
#guessing_game()

