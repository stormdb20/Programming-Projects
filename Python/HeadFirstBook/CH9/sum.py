#list of numbers that we need the sum of
marbles=[10,13,39,14,41,9,3]
#create function for computing sum of list
def recursive_compute_sum(list):
    #Compare length of list to o and if its true return 0
    if len(list) == 0:
        return 0
    #if not zero slice the first thing in list then 
    else:
        first=list[0]
        rest=list[1:]
        sum= first + recursive_compute_sum(rest)
        return sum
#Global variable to call recursive compute sum function passing the marbles list to it then printing sum
sum= recursive_compute_sum(marbles)
print('The total sum is', sum)