#Larry Baucum ENT-1770-LD01
#prompt user for item prices
num1=int(input("Enter item 1 price "))
print("your price is ",num1)
num2=int(input("Enter item 2 price "))
print("your price is ",num2)
num3=int(input("Enter item 3 price "))
print("your price is ",num3)
num4=int(input("Enter item 4 price "))
print("your price is ",num4)
num5=int(input("Enter item 5 price "))
print("your price is ",num5)
#variable for subtotal
num7=(num1+num2+num3+num4+num5)
#print subtotalof all items
print('Subtotal=',num7)
#print amount of sales tax
print("Sales Tax 7%")
#my variable for sales tax
num6=.07
#print total of all items with tax
print("Your Total=",num6*num7+num7)

