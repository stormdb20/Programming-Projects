#This program will take a test score from the user and print their letter grade

#Get test score from the user
test_score = int(input("Enter your test score: "))

#If statement to check if score is in range of 0-100
if test_score < 0 and test_score > 100:
                  
    print("Enter a score from 0-100 please")

#Elif statements for the different letter grades depending on the score entered
elif test_score < 60:
    print("Your grade is F")
    print("Good luck on your next test")


elif test_score < 70:
    print("Your grade is D")
    print("Good luck on your next test")


elif test_score < 80:
    print("Your grade is C")
    print("Good luck on your next test")


elif test_score < 90:
    print("Your grade is B")
    print("Good luck on your next test")


else:
    print("Your grade is A")
    print("Good luck on your next test")


print("Done")
