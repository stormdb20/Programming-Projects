#This program will get the users age and name. Then it will output the year they turn 100.


#Try code
try:
    
    #Static Variables
    current_year = 2023


    #Greeting
    print("Welcome to the 100 year old calculator!")

    #prompt the user for age and name.
    name = input("What is your name? ")
    age = int(input("What is your age? "))

    #While loop to make sure the user inputs an age in the allowable range.
    #while (age < 1) or (age > 100):

        #age = int(input("What is your age? "))



    #calculate the difference of the age to 100.
    age_diff = 100 - age


    #add the age difference to the year variable.
    year_100 = current_year + age_diff

    #outpu the year the user will be 100
    print(name,"the year you will be 100 years old is", year_100)

#Exceptions
except ZeroDivisionError:
    
    print("Can't divide by zero try again")

