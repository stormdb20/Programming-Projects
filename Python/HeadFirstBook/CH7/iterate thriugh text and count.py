#import text from text file
import CH1text
#Function to count amount of sentences using punctuation
def count_sentences(text):
    #local to hold count
    count=0
#interate through the text counting punctuation and increasing count using or
    for char in text:
        if char =='.' or char == '?' or char == ';' or char == '!':
            count= count+1
# Return the count after iterating through the text    
    return count

#also the more efficient way to check for specific characters is to use in
def count_sentences(text):
    #local to hold count
    count=0
    #variable to hold punctuation characters
    terminals='.?!;'
#interate through the text counting punctuation and increasing count using in
    for char in text:
        if char in terminals:
            count= count+1
# Return the count after iterating through the text  
    return count

count_sentences(CH1text)
