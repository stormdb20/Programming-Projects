#Import the turtle module
import turtle 
#Variable to hold turtle
slowpoke=turtle.Turtle()
#Change turtle attribute to turtle
slowpoke.shape('turtle')
slowpoke.color('blue')

slowpoke.pencolor('blue')
slowpoke.penup()
slowpoke.setposition(-120,0)
slowpoke.pendown()
slowpoke.circle(50)

slowpoke.pencolor('red')
slowpoke.penup()
slowpoke.setposition(120,0)
slowpoke.pendown()
slowpoke.circle(50)


#Monitors the turtle and shuts it down when needed
turtle.mainloop()