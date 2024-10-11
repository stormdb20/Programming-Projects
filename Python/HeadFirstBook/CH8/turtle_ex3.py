#Import the turtle module
import turtle 
#Variable to hold turtle
slowpoke=turtle.Turtle()
#Change turtle attribute to turtle
slowpoke.shape('turtle')
slowpoke.color('blue')

def make_shape(t,sides):
    angle=360/sides
    
    for i in range(0,sides):
        t.forward(100)
        t.right(angle)
        
make_shape(slowpoke,2)
make_shape(slowpoke,4)
make_shape(slowpoke,6)
make_shape(slowpoke,8)



#Monitors the turtle and shuts it down when needed
turtle.mainloop()