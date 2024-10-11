#Import the turtle module
import turtle 
#Variable to hold turtle
slowpoke=turtle.Turtle()
#Change turtle attribute to turtle
slowpoke.shape('turtle')
slowpoke.color('blue')

for i in range(5):
    slowpoke.forward(100)
    slowpoke.right(144)


#Monitors the turtle and shuts it down when needed
turtle.mainloop()