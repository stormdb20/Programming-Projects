#Larry Baucum INT-1111

#defining function for input of full name and output of the initials
def main():
#Variable for full name input
  F=input('Enter Full Name With Spaces: ')
#Splitting the name and putting it into a list
  Name = F.split()
#Printing the initials from the list
  print('Your Initials are ', Name[0][0], Name[1][0], Name[2][0])
#Calling the function
main()
  
