#Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.#
#>>> # Test Case 1: enter the numbers 3 and 5
# Test Case 2: enter the numbers 3 and 0
# Test Case 3: enter the numbers 2 and 5

#Gets two numbers from the users that are greater than zero
firstNum = int(input("Enter a non zero number: "))
secondNum = int(input("Enter a non zero number: "))

#Checks if the numbers are less than zero
if firstNum <= 1 or secondNum <= 1:
    print("Both numbers must be positive")

#Check if first num is less than or equal to 2 and the first and second numbers are not equal  
elif (firstNum <= 2) and (firstNum != secondNum):
    print("Second number raised to the first number: ", secondNum**firstNum)

#Checks if the numbers are equal to eachother
elif (firstNum == secondNum):
    print("The sum of these numbers is: ", firstNum + secondNum)

#else to output the product of the numbers    
else:
    print("The product of the two numbers is: ", firstNum * secondNum)
    
print("Done")