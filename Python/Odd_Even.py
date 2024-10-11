#This program will take an int value from the user and output if the value is even or odd

    
#Prompt the user
user_val = int(input("Enter an int value please: "))

#check for even or odd using modulus 2
check =  user_val % 2

#Conditional if/else statement to check for even/odd and output  result
if check == 0:
    print("Even")
        
else:
    print("Odd")