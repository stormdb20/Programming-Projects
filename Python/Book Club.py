#Larry Baucum INT-1111
#Variable for how many books have been purchased
books=int(input("How many books have you purchased this month? "))
#if statements for award points you get 
if books >= 8:
  print("You have earned 60 points")
elif books == 6:
  print("You have earned 30 points")
elif books == 4:
  print("You have earned 15 points")
elif books == 2:
  print("You have earned 5 points")
else:
  print("You have earned 0 points")
