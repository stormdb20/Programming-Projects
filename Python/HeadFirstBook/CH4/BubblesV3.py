#create list for bubble scores
scores= [60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69,
         34, 55, 51, 52, 44, 51, 69, 64, 66, 55, 52, 61,
         46, 31, 57, 52, 44, 18, 41, 53, 55, 61, 51, 44]
#create list for bubble test costs
costs=[.25, .27, .25, .25, .25, .25, .33, .31, .25, .29, .27, .22,
       .31, .25, .25, .33, .21, .25, .25, .25, .28, .25, .24, .22,
       .20, .25, .30, .25, .24, .25, .25, .25, .27, .25, .26, .29]
#Variable to hold the high score
high_score=0
#Get the length of the list
length=len(scores)
#For loop to iterate through the list
for i in range(length):
 #Print bubble solution with test number and score
    print('Bubble Solution #' + str(i),'score:',scores[i])
    #For loop to track high score
    if scores[i] > high_score:
           high_score=scores[i]
#Print number of tests and high score
print('Number of tests:', length)
print('The highest test score is', high_score)
#Empty list for tests with high score and iteration and comparison arguments to find those tests
best_solutions=[]
for i in range(length):
   if high_score == scores[i]:
      best_solutions.append(i)
#Print the list containing the highest score tests      
print('The solutions with the highest score:', best_solutions)   
#Compare indexes in list to see which of the high scores has the lowest cost
cost=100.0
most_effective=0
for i in range (len(best_solutions)):
    index=best_solutions[i]
    if cost > costs[index]:
      most_effective=index
      cost=costs[index]
#Print the most cost effective solution and the price with message
print('Solution', most_effective,
      'is the most effective with a cost of', costs[most_effective], 'cents')