#import random and turtle modules with list to hold turtles
from operator import truediv
import turtle
import random 

turtles = list()
# function to position and setup racing turtles
def setup():
    global turtles
    #will hold x coordinate for start position
    startline= -620
    #Change screen object attributes(background, size)
    screen=turtle.Screen()
    screen.setup(1290,720)
    screen.bgpic("pavement.gif")
    #Lists for turtle start position on ycor and turtle color
    turtle_ycor=[-40, -20, 0, 20, 40]
    turtle_color=['blue', 'red', 'purple', 'brown', 'green']
    #Iterate through lists creating turtles with color, start position, and pen up/down then add to turtles list
    for i in range(0, len(turtle_ycor)):
        new_turtle= turtle.Turtle()
        new_turtle.shape('turtle')
        new_turtle.penup()
        new_turtle.setpos(startline, turtle_ycor[i])
        new_turtle.color(turtle_color[i])
        new_turtle.pendown()
        turtles.append(new_turtle)
#Function to make turtles race by setting winner variable to false and looping until its true condition is met
def race():
    global turtles
    winner=False
    finishline=590
#While loop to move turtles a random amount forward until theres a winner
    while not winner:
        for current_turtle in turtles:
            move=random.randint(0,2)
            current_turtle.forward(move)
#compare current turtle position with finishline then output winner from their color
            xcor=current_turtle.xcor()
            if (xcor >= finishline):
                winner=True
                winner_color=current_turtle.color()
                print('The winner is', winner_color[0])
#Call setup and race functions and turtle loop
setup()
race()
turtle.mainloop()