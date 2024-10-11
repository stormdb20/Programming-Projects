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
#creating file to put assessment value and property tax in
    property_info=open('tax.txt', 'w')
#writing property info to file
    property_info.write('This is your assessment value:\n')
    property_info.write(str(tax_formula) + '\n')
    property_info.write('Your property tax is:\n')
    property_info.write(str(assessment_tax) + '\n')
    property_info.close()
    print('A file has been created and saved to the computer disk')
tax()
    
