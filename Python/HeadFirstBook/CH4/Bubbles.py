#create list for bubble scores
scores= [60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69,
         34, 55, 51, 52, 44, 51, 69, 64, 66, 55, 52, 61,
         46, 31, 57, 52, 44, 18, 41, 53, 55, 61, 51, 44]
#variable to track index
i=0
#length of the list
length= len(scores)
#loop for printing the test solutions with scores from list
while i<length:
    print('Bubble Solution #' + str(i),'score:',scores[i])
#increment the variable tracking index position
    i=i+1


    