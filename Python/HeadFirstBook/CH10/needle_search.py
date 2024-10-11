
#iterate throught the files
for i in range(0,1000):
    #variable for holding the current file
    filename=str(i)+'.txt'
    #var to read in the current file
    file= open(filename, 'r')
    #var to read the current file
    text=file.read()
    #compare the text of current file with string 'needle' 
    if 'needle' in text:
        print('Found the needle in file', + str(i) + '.txt')
    #close the file
    file.close()