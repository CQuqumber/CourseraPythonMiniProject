

import simplegui
import random
import math

# initialize global variables used in your code
num_range = 100
secret_num = 0
num_can_guess = 0


# helper function to start and restart the game
def new_game():  
    global num_range
    global secret_num
    global num_can_guess
    
    secret_num = random.randrange(0, num_range)
    
    if num_range == 100 : 	
        num_can_guess = 7
    elif num_range == 1000 :
        num_can_guess = 10
      

    print "New game. The range is from 0 to", num_range
    print "Number of remaining guesses is ", num_can_guess, "\n"
    pass


# define event handlers for control panel
def range100():
    global num_range
    num_range = 100 # button that changes range to range [0,100) and restarts
    new_game() 


def range1000():
    global num_range
    num_range = 1000 # button that changes range to range [0,1000) and restarts
    new_game()


    
def input_guess(guess):    
    
    global num_can_guess
    global secret_num 
    
    won = False
    
    print "You guessed: ",guess
    guesses_left = num_can_guess - 1
    print "Number of remaining guesses is ", num_can_guess
    
    if int(guess) == secret_num:       
        won = True
    elif int(guess) > secret_num:
        result = "Lower!"
    else:
        result = "Higher!"                
        
        
    if won:
        print "That is correct! Congratulations!\n"
        new_game()
        return
    elif guesses_left == 0:
        print "Game over. You didn't guess the number in time!"   
        new_game()
        return
    else:
        print result
        pass
            
    
# create frame
f = simplegui.create_frame("Game: Guess the number!", 200, 200)

# register event handlers for control elements
f.add_button("Range is [0, 100)", range100, 100)
f.add_button("Range is [0, 1000)", range1000, 100)	
f.add_input("Enter your guess", input_guess, 100)

# call new_game and start frame
new_game()
f.start()



# always remember to check your completed program against the grading rubric
