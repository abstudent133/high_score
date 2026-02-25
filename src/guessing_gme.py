#IC 1st guessing number game 
#import random 
import random
#definging score
score = 0
# show the user hello you have entered the numbers guessing game 
print("hello you have entered the numbers guessing game")
# the point of this game is to guess a number between 1 - 1000
print("the point of this game is to guess a number between 1- 1000")
# quit is equal to false 
quit == False
# while quit is equal to false let the game contiune 
while quit != True: 
#   get a random number in the range of 1 - 1000
    random_number = random.randint(1, 1000)
#   show the user im thinking abt a number from 1 - 1000 how abt you guess
    print("Im thinking about a number from 1 - 1000:")
#   asking the user guess a number bewtween 1 - 1000 
    guess_input = input("guess a number between 1-1000:")
#   save this as a variable under the name guess 
    guess = int(guess_input)
    if guess == random_number:
         score += 10
         print(score)
#       # if (guess >= random_num - 10 and guess < random_num) or (guess <= random_num + 10 and guess > random_num)
            #add seven to the score 
    elif (guess >= random_number - 10 and guess < random_number) or (guess <= random_number + 10 and guess > random_number):
            #add seven to the score 
            score += 7 
            print(score)
        # if (guess >= random_num - 20 and guess < random_num) or (guess <= random_num + 20 and guess > random_num)
    elif (guess >= random_number - 20 and guess < random_number) or (guess <= random_number + 20 and guess > random_number):
          #add five to score
          score += 5 
          print(score)
        # if (guess >= random_number - 30 and guess < random_number) or (guess <= random_number + 30 and guess > random_number)
    elif (guess >= random_number - 30 and guess < random_number) or (guess <= random_number + 30 and guess > random_number):
#         # add three to score
        score += 5 
        print(score)
        # if (guess >= random_num - 40 and guess < random_num) or (guess <= random_num + 40 and guess > random_num)
    elif (guess >= random_number - 40 and guess < random_number) or (guess <= random_number + 40 and guess > random_number):
            # add two to score
        score += 2
        # if (guess >= random_num - 50 and guess < random_num) or (guess <= random_num + 50 and guess > random_num)
    elif (guess >= random_number - 50 and guess < random_number) or (guess <= random_number + 50 and guess > random_number):
            # add one to score
        score += 1
        #else:
    else:
            #show the user you got no points
        print("you got no points")
    # ask user if they want to play again (yes/no)
    input("do you want to play again yes or no:")
        # if yes
    if "yes":
            # quit equals true
        print("goodbye")
        quit == True
        break
        # else:
    else:
           # quit still equals false  
        quit == False  
else:
     quit == True 
     print("goodbye")

# at end, send back to signed in menu   
quit == True
