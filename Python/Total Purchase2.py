#Larry Baucum INT-1111

#Define function
def main():
#Input for item prices
    i1=int(input('How much is your item: '))
    i2=int(input('How much is your item: '))
    i3=int(input('How much is your item: '))
    i4=int(input('How much is your item: '))
    i5=int(input('How much is your item: '))
#Variable for adding item prices
    Subtotal=i1+i2+i3+i4+i5
#Variable for calculating sales tax
    Tax=Subtotal*.07
#Variable for calculating the total
    Total=Subtotal+Tax
#Printing the subtotal, sales tax, and total
    print('Your subtotal is $', Subtotal)
    print('Your sales tax is 7%')
    print('Your total is $', Total)
#Calling the function
main()
