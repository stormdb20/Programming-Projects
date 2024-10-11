#Larry Baucum INT-1111
#Defining function for monthly and annual cost of automobile
def cost():
#Declaring input variables for the various expenses
  loan=float(input("Enter loan amount:"))
  insurance=float(input("Insurance:"))
  gas=float(input("Enter gas amount:"))
  oil=float(input("Enter oil amount:"))
  tires=float(input("Enter tire amount:"))
  maintenance=float(input("Enter maintenance amount:"))
#Declaring variable for the sum of all expenses
  monthly=(loan+insurance+gas+oil+tires+maintenance)
#Printing the monthly and annual expenses for the automobile
  print("Your monthly total is ",monthly)
  annual=(monthly*12)
  print("Your annual total is ",annual)
#Calling the function
cost()
