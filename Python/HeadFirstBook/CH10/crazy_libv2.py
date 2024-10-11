#function for making crazy lib
def make_crazy_lib(filename):
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
#main function to call make crazy lib function
def main():
    #var to call make crazy lib and pass it the filename to be used 
    lib=make_crazy_lib('random.txt')
    print(lib)
#compare to make sure the main program should run
if __name__=='__main__':
    main()    
