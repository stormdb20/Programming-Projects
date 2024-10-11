#Color game While loop
def color_game():
    color='blue'
    guess=''
    guesses=0

    while guess != color:
        guess= input("What color am I thinking of from yellow, blue, and red? ")
        guesses= guesses+1
    if guesses ==1:
        print(' You got it! It took you', guesses, 'guess')
    else: 
        print(' You got it! It took you', guesses, 'guesses')

color_game()