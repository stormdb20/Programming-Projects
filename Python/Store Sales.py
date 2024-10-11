#Larry Baucum INT-1111

#Define the function
def main():
#creating my list
    w_profit=[]
#Variable for inputting how many days to get sales numbers
    x=int(input('How many week days: '))
#For loop for getting sales of the each work day
    for n in range(x):
#Variable for inputting daily sales amounts
      sales=int(input('Enter Sales Amount:'))
#Putting the sales amounts in the weekly profit list
      w_profit.append(sales)
#Printing the total sales of the week
    print('The total of our sales for the week  is $', sum(w_profit))
#Calling the function
main()
