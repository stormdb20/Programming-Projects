#Import our text from another python file also called a module
import CH1text
#Function to count amount of sentences using punctuation
def count_sentences(text):
    #local to hold count
    count=0
#interate through the text counting punctuation and increasing count 
    for char in text:
        if char =='.' or char == '?' or char == ';' or char == '!':
            count= count+1
# Return the count after iterating through the text    
    return count
#Function for text readability
def compute_readability(text):
    total_sentences=0
    total_words=0
    total_syllables=0
    score=0
    #split the words of text file into a list
    words=text.split()
    #Get the length of the words list to know the total words amount
    total_words=len(words)
    #
    total_sentences=count_sentences(text)
    print(total_words, 'words')
    print(total_sentences, 'sentences')
#Call readability function passing the ch1 text to the function
compute_readability(CH1text.text)
