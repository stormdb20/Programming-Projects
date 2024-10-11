#Larry Baucum INT-1111
#Define the function max with arguments
def max(value1,value2):
    
#IF and else statements for which value to print
    if value1 > value2:
        print("The greater number is:", value1)
    else:
        print("The greater number is:", value2)
#Calling the function while asking for the integer values
max(value1=int(input("Enter Value1:")), value2=int(input("Enter Value2:")))

