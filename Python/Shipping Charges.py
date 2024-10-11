#Larry Baucum INT-1111
#variable with input for package weight
weight=int(input("How much does your package weigh? "))
#if statements for weight. Also the math for price
if weight > 10:
  print("Your shipping rate is: $4.75")
  print("Your shipping price is: $",4.75*weight)
elif weight > 6 <= 10:
  print("Your rate per pound is: $4.00")
  print("Your shipping price is: $", 4*weight)
elif weight > 2 <= 6:
  print("Your rate per pound is: $3.00")
  print("Your shipping price is: $", 3*weight)
elif weight <= 2:
  print("Your rate per pound is: $1.50")
  print("Your shipping price is: $", 1.5*weight)
