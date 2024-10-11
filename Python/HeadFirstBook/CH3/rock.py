#imported the random code and setup winner variable for the game.

import random

winner=''
#Created random number selection and if statement to assign random numbers to value under the variable computer choice

random_choice= random.randint(0,2)

if random_choice==0:
    computer_choice='rock'

elif random_choice==1:
    computer_choice= 'paper'

else:
    computer_choice='scissors' 

 #Check that the input is valid
user_choice= ''

while (user_choice != 'rock' and
    user_choice != 'paper' and
    user_choice != 'scissors'):
    user_choice= input('rock, paper, or scissors? ')
#If statement to compare user and computer choice afterwards assigning the winner variable with a tie or winner

if computer_choice==user_choice:
    winner='Tie' 

elif computer_choice=='rock' and user_choice=='scissors':
    winner='Computer :('

elif computer_choice=='scissors' and user_choice=='paper':
       winner='Computer :('

elif computer_choice=='paper' and user_choice=='rock':
    winner='Computer :('
    
else:
    winner='User :)'
 
#If statement for a nice output to the user on if it was a tie or who won
   
if winner == 'Tie':
    print('We both chose', computer_choice +', Play Again. :(')

else:
    print(winner, 'Wins. The computer chose', computer_choice + '.') 