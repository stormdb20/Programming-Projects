#import python time module
import time
#function to get fibonacchi numbers
def fibonacchi(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacchi(n-1)+fibonacchi(n-2)
    
#iteration for timing a fibonacchi count in increments of 5 until number 100 reached
for i in range(20,55,5):
    #variable to start timer
    start=time.time()
    #var for fibonacchi results
    result=fibonacchi(i)
    #var for stop timer
    end=time.time()
    #var for compute duration
    duration=end-start
    print(i, result, duration)
    
        
