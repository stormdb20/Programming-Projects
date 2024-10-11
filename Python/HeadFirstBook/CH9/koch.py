import turtle
#function to setup pencil with attributes and move to a location
def setup(pencil):
    pencil.color('blue')
    pencil.penup()
    pencil.goto(-200,100)
    pencil.pendown()
#recursive function based off of the order that changes the angle based on the order after the size and order have been reduced  
def koch(pencil, size, order):
    if order == 0:
        pencil.forward(size)
        
    else:
        for angle in [60, -120, 60 , 0]:
            koch(pencil, size/3, order-1)
            pencil.left(angle)
#main function that makes the pencil variable a turtle and sets the size and order passing the values to koch function
def main():
    pencil=turtle.Turtle()
    setup(pencil)
    
    order=4
    size=400
    koch(pencil, size, order)
#check if main program and if so runs the turtle and turtle tracer which manipulates turtle speed  
if __name__ == '__main__':
    main()
    turtle.tracer(100)
    turtle.mainloop()