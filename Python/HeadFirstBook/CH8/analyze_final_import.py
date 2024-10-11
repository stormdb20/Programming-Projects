"""the analyze module uses the FLesch-Kincaid readability test to analyze text and
produce a readability score. This score is then converted into a grade-based readability category.

"""
#Syllable counting function
def count_syllables(words):
    """This function takes a list of words and returns a total count of syllables
        across all words in the list.
    """
    count=0
#Iterate throught the current word passing the word to count syllables function and return the count
    for word in words:
            word_count=count_syllables_in_word(word)
            count=count+word_count
    return count
#Function for counting syllables
def count_syllables_in_word(word):
    """This function takes a word in the form of a string and returns the number 
        of syllables. Note this function is a heuristic and may not be 100% accurate.
    """
    count=0
#variable to hold characters to be sliced and slicing variable
    endings='.,?;:!'
    last_char=word[-1]    
#compare word string with endings chars and if chars are in the word slice
    if last_char in endings:
        processed_word=word[0:-1]
    else:
        processed_word=word
#Get length of the word and compare to see if 1 should be returned
    if len(processed_word) <= 3:
        return 1
#check if word has e and slice if it does
    if processed_word[-1] in 'eE':
        processed_word=processed_word[:-1] 
    else:
        processed_word=word   
#make variable to hold vowels and then iterate through words to compare characters of terminal variable 
    vowels='aeiouAEIOU'
 #variable for checking if previous character was vowel
    prev_char_was_vowel= False
#Iterate through current string and check if ccurrent char in vowels 
    for char in processed_word:
        if char in vowels:
#Check if previous char was vowel and if not increment count
            if not prev_char_was_vowel:
                count=count+1
 #set to true no matter what
            prev_char_was_vowel= True
#if not a vowel set prev_char_was_vowel variable to false
        else:
            prev_char_was_vowel= False
    if processed_word[-1] in 'yY':
        count=count+1
    return count

#Function to count amount of sentences using punctuation
def count_sentences(text):
    """This function counts the number of sentences ina a string of text using period,
        semicolon, question mark and exclamation mark as terminals.
    """
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
#function for outputting results of readability
def output_results(score):
    """This function takes a Flesch-Kincaid score and prints the correspondin reading level.
    """
    if score >= 90:
        print('Reading level of 5th grade')
    elif score >=80:
        print('Reading level of 6th grade')
    elif score >=70:
        print('Reading level of 7th grade')
    elif score >=60:
        print('Reading level of 8-9th grade')
    elif score >=50:
        print('Reading level of college student')
    else:
        print('Reading level of college graduate')
    
#Function for text readability
def compute_readability(text):
    """This function takes a text steinf of any length and prints out a
        grade-based readability score.
    """
    total_sentences=0
    total_words=0
    total_syllables=0
    score=0
    #split the words of text file into a list
    words=text.split()
    #Get the length of the words list to know the total words amount
    total_words=len(words)
    #Call the sentence and syllables functions then print values 
    total_sentences=count_sentences(text)
    total_syllables=count_syllables(words)
    #Readability score formula
    score= (206.835 - 1.015 * (total_words/total_sentences)
            - 84.6 * (total_syllables/total_words))
    
    output_results(score) 


if __name__ == '__main__':
    #Import our text from another python file also called a module
    import CH1text
    print('Chapter1 Text:') 
    #Call readability function passing the ch1 text to the function
    compute_readability(CH1text.text)