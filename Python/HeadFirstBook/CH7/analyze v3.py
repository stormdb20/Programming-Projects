#Import our text from another python file also called a module
import CH1text
#Syllable counting function
def count_syllables(words):
    count=0
    
    for word in words:
        word_count=count_syllables_in_word(word)
        count=count+word_count
        return count

def count_syllables_in_word(word):
    count=0
#Get length of the word and compare to see if 1 should be returned
    if len(word) <= 3:
        return 1
#make variable to hold vowels and then iterate through words to compare characters of terminal variable 
    vowels='aeiouAEIOU'
    for char in word:
        if char in vowels:
            count=count+1
    return count

#Function to count amount of sentences using punctuation
def count_sentences(text):
    #local to hold count
    count=0
   #variable to hold punctuation characters
    terminals='.?!;'
#interate through the text counting punctuation and increasing count using in to compare
    for char in text:
        if char in terminals:
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
    #Call the sentence count function 
    total_sentences=count_sentences(text)
    print(total_words, 'words')
    print(total_sentences, 'sentences')
#Call readability function passing the ch1 text to the function
compute_readability(CH1text.text)