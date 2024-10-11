#import the sys module to allow command line to use the argv attribute to list whats typed in the command line for python
import sys
#function for making crazy lib
def make_crazy_lib(filename):
   #try exception  
    try:
        #open the filename passed to the function and read it in the program
        file=open(filename,'r')
        #variable to hold text currently an empty string
        text=''
        #iterate through the file and use process line to concantenate the text
        for line in file:
            text=text + process_line(line) + '\n'
        #close the file and return the text
        file.close()
        return text
#exceptions if error(exception) is found for three different situations
    except FileNotFoundError:
        print("Sorry, couldn't find ", filename + '.')
        
    except IsADirectoryError:
        print('Sorry', filename, 'is a directory.')
        
    except:
        print("Sorry, could not read", filename)
        
        

#list to hold placeholder names
placeholders=['NOUN', 'VERB', 'VERB_ING', 'ADJECTIVE']
#function to process the lines in a file and return the line
def process_line(line):
    #use global placeholders list
    global placeholders
    #var to hold empty string
    processed_line=''
    #var to split the words in a line
    words=line.split()
    #iterate through words
    for word in words:
        #strip the punction off the placeholder words
        stripped=word.strip('?!.,;')
        #compare stripped word with placeholders 
        if stripped in placeholders:
            #get input from user concantenate input with stripped word and added string text
            answer=input('Enter a ' + stripped + ':')
            #var to add user input to processed line
            processed_line= processed_line + answer + ' '
            #compare end of word with string if true add end of word back to the word
            if word[-1] in '?!.,;':
                processed_line=processed_line + word[-1] + ' '
            else:
                #var to return processed line with current word
                processed_line=processed_line + ' '
        else:
            processed_line=processed_line + word + ' '
    return processed_line + '\n'

#function to save completed crazy lib to a file
def save_crazy_lib(filename,text):
    try:
     #open the filename and write to it
        file=open(filename, 'w')
     #pass the text string to the file
        file.write(text)
        file.close()
    except:
        print("Sorry, couldn't write file", filename)
#main function to call make crazy lib function
def main():
    #compare to check if there are two arguments if not then print message asking for two
    if len(sys.argv) !=2:
        print("crazy.py <filename>")
    #otherwise the filename is command line argument index 1
    else:
        filename= sys.argv[1]
        lib= make_crazy_lib(filename)
        if (lib !=None):
            save_crazy_lib('crazy' + filename, lib)
        
    #name of file to be used
    filename='lib.txt'
    #var to call make crazy lib and pass it the filename to be used 
    lib=make_crazy_lib(filename)
    #comparison to test if lib has a text file if not it will return none
    if (lib !=None):
        #passing value to save crazy lib func
        save_crazy_lib('crazy_' + filename, lib)
             
#compare to make sure the main program should run
if __name__=='__main__':
    main()    
