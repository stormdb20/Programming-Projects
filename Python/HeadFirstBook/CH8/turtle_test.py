#Import the turtle module
import turtle 
#Variable to hold turtle
slowpoke=turtle.Turtle()
#Change turtle attribute to turtle
slowpoke.shape('turtle')
slowpoke.color('blue')
#Second turtle pokey and changed attributes
pookey=turtle.Turtle()
pookey.shape('turtle')
pookey.color('red')

#Function for making a square with turtle
def make_square(the_turtle):
    for i in range(0,4):
    #Give the turtle marching directions
        the_turtle.forward(100)
        the_turtle.right(90)
#Function for making a spiral
def make_spiral(the_turtle):
    for i in range (0,36):
        make_square(the_turtle)
        the_turtle.right(10)
#call function for each turtle with direction change to pokey
make_spiral(slowpoke)
pookey.right(5)
make_spiral(pookey)

#Monitors the turtle and shuts it down when needed
turtle.mainloop()