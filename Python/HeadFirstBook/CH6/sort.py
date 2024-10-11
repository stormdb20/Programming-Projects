#function to sort scores in ascending order
def bubble_sort(scores):
    #variable to start first pass of list
    swapped=True
#nested loop to make passes while swapped is true
    while swapped:
        swapped=False
#Compare and swap values in the list as needed
        for i in range(0, len(scores)-1):
#if the greater than is switched to less than you can get descending order instead
            if scores[i]> scores[i+1]:
                #Variable swap
                temp=scores[i]
                scores[i]=scores[i+1]
                scores[i+1]=temp
                swapped=True
#List of scores to be passed to sorting function
scores=[60,50,60,58,54,54,
        58,50,52,54,48,69,
        34,55,51,52,44,51,
        69,64,66,55,52,61,
        46,31,57,52,44,18,
        41,53,55,61,51,44]
#Call function to sort the list scores
bubble_sort(scores)
print(scores)

smoothies=['coconut','strawberry','banana','pineapple']
bubble_sort(smoothies)
print(smoothies)

