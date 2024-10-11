#Larry Baucum INT-1111
#Define function for weight loss in caloric deficit
def calorie():
#Declare local variables for input of starting weight and months
    x=int(input("Enter Starting Weight:"))
    month=0
#While loop for each months expected weight loss
    while month <= 5:
#Creating expression for the month and weight variables for the while loop
        month+=1
        x-=4
#Print what month and expected weight is 
        print("For month", month,"Your expected weight is", x, "lbs")
#Calling the function for weight loss
calorie()
