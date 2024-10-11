#Larry Baucum INT-1111
#variable with input for purchased packages
package=int(input("How many packages have you purchased? "))
#subtotal variable
subtotal=package*99
#40% discount variable
discount40=.40*subtotal
#30% discount variable
discount30=.30*subtotal
#20% discount variable
discount20=.20*subtotal
#10% discount variable
discount10=.10*subtotal

#elif statements for determining the discount to be applied
if package >= 100:
  print("Your discount is 40%")
  print("Total=", subtotal-discount40)
elif package in range(50,99):
  print("Your discount is 30%")
  print("Total=", subtotal-discount30)
elif package in range(20,49):
  print("Your discount is 20%")
  print("Total=", subtotal-discount20)
elif package in range(10,19):
  print("Your discount is 10%")
  print("Total=", subtotal-discount10)
else:
  print("No discount")
  
