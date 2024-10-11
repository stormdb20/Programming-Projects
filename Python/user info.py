#Larry Baucum INT-1111
#function for the user info
def main():
#variable for inputing age
    age=int(input("Please Enter Your Age:"))
#if statement for age over or under 18
    if age > 17:
#variables for inputting age and description
        life=int(input('Enter Your Age: '))
        descript=(input('Enter a brief description: '))
#creating the user info file to be written to
        x=open('userinfo.txt', 'w')
#writing the user input for age and description
        x.write(str(life) + '\n')
        x.write((descript) + '\n')
#closing the program
        x.close()
#else statement for the person being under 18
    else:
#Open and write to the error file
        y=open('error.txt', 'w')
        y.write('Terminate the program')
#close the program
        y.close()
#calling the function
main()
        
