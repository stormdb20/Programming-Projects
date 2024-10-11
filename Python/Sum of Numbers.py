#Larry Baucum INT-1111


#define function
def main():
#Create empty list
  L=[]
#Input for single digits with no spaces
  pet=input('Enter single digit numbers with no spaces: ')
#For loop to separate the number and put them in a list
  for x in pet:
#Printing the indiviual numbers to make sure the correct numbers are there  
    print(x)
#Appending the numbers into the list and converting them into integers
    L.append(int(x))
#Printing the list with the numbers separated 
  print(L)
#Print the sum of the numbers in the list
  print('The sum of your numbers is: ', sum(L))
  
#Call the function
main()
        
    
