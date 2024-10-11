#Larry Baucum INT-1111
#Defining function for creating the txt file
def numbers():
    #opening a file called numbers.txt
    integers= open('numbers.txt', 'w')

    #variables for integer input
    num1=(int(input('enter first number:')))
    num2=(int(input('enter second number:')))
    num3=(int(input('enter third number:')))

    #writng inputted numbers in the file
    integers.write(str(num1) + '\n')
    integers.write(str(num2) + '\n')
    integers.write(str(num3) + '\n')

    #Closing file
    integers.close()
    #printing that data has been written to the file
    print('Inputted integers have been written to the file')
#Calling the function
numbers()

#Define a function for calculating the total of the integers
def calculate():
#opening the file to be read
    integers= open('numbers.txt', 'r')

#variables for reading lines in the file and converting them from str to int
    int1=int(integers.readline())
    int2=int(integers.readline())
    int3=int(integers.readline())
    
#closing the file
    integers.close()
#print the sum of the numbers
    print('Here is the total of your integers:', int1+int2+int3)
#call the function
calculate()

