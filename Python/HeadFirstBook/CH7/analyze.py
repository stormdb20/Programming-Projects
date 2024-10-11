#Import our text from another python file also called a module
import CH1text
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
    print(words)
    print(total_words, 'words')
#Call readability function passing the ch1 text to the function
compute_readability(CH1text.text)
