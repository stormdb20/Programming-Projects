#import time module
import time
#empty dictionary to hold fibonacchi numbers cache is commonly used name in data storage
cache={}
#function to compute and check cache for fibonacchi numbers and return results
def fibonacchi(n):
    #use global cache 
    global cache
    #check if result in cache and return if it is
    if n in cache:
        return cache[n]
    
    #fibonacchi computation using recursion
    if n==0:
        result=0
    elif n==1:
        result=1
    else:
        result= fibonacchi(n-1) + fibonacchi(n-2)
    #assign result to key in cache which is whatever the current fibonacchi number is
    cache[n]= result
    return result

#start timer
start=time.time()
#iterate through the numbers computing and saving the numbers
for i in range(1,101):
    result=fibonacchi(i)
    print(i, result)
    
#stop timer
finish=time.time()
#variable to hold and compute duration
duration=finish-start

print('Compute all 100 in', duration, 'seconds')