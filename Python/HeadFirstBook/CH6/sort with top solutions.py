#function to sort scores in ascending order
def bubble_sort(scores, numbers):
    #variable to start first pass of list
    swapped=True
#nested loop to make passes while swapped is true
    while swapped:
        swapped=False
 #Compare and swap values in the list as needed
        for i in range(0, len(scores)-1):
#if the less than is switched to greater than you can get ascending order instead
            if scores[i]< scores[i+1]:
                #Variable swap
                temp=scores[i]
                scores[i]=scores[i+1]
                scores[i+1]=temp
#When score list is swapped we swap numbers list also to kepp index positions of values
                temp=numbers[i]
                numbers[i]=numbers[i+1]
                numbers[i+1]=temp
                swapped=True
#List of scores to be passed to sorting function
scores=[60,50,60,58,54,54,
        58,50,52,54,48,69,
        34,55,51,52,44,51,
        69,64,66,55,52,61,
        46,31,57,52,44,18,
        41,53,55,61,51,44]
#Get length of the list
number_of_scores=len(scores)
#Get range of list from 0 ti the end then turn that into a list 
solution_numbers=list(range(number_of_scores))
#Call function to sort the list scores
bubble_sort(scores,solution_numbers)
print(scores)
#print report with top 5 solutions
print('Top Bubble Solutions')
#get the top 5 solutions by iterating the list 
for i in range(0,5):
#print the final position of the solution using i+1, the index of the value from solution_numbers, and the score from scores[i] 
    print(str(i+1) +')',
          'Bubble Solution #' + str(solution_numbers[i]),
          'score:', scores[i]) 

