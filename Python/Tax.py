#Larry Baucum INT-1111
#Defining function for property tax for the assessment value of property
def tax():
#Declaring input variable for property value
    property_value=float(input("Enter Property Value:$"))
#Declare variable for calculating the assessment value
    tax_formula=(property_value*.60)
#Printing the assessment value of the property
    print("This is your assessment value:",tax_formula)
#Declare variable for calculating property tax
    assessment_tax=(tax_formula*.72*.01)
#Printing the property tax
    print("Your property tax is:$", assessment_tax)
#Calling the function
tax()
    
