#Larry Baucum INT-1111

#define function
def main():
#Create an empty list
    one=[]
#variable for how many numbers to be inputted
    x=int(input('How many numbers? '))
#For loop to keep asking for numbers until the specified amount is reached
    for n in range(x):
#variable for inputting numbers
        numbers=int(input('Enter Number:'))
#appending the input into the list
        one.append(numbers)
#printing the smallest number in the list
    print('The smallest number is:', min(one))
#printing the boggest number in the list
    print('The biggest number is:', max(one))
#printing the sum of all numbers in the list using sum
    print('The sum of all the numbers is:', sum(one))
#print the average of all the numbers in the list using sum and len
    print('The average of the list is:', sum(one)/len(one))
#Calling the function
main()
        
