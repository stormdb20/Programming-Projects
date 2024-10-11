#print message
print('Get those dogs ready')
#define our function
def bark(name, weight):
    if weight > 20:
        print(name,'Says WOOF WOOF')
    else:
        print(name, 'Says woof woof')
#Call/invoke our function and pass arguments to it
bark('codie', 40)
bark('Troy', 35)
bark('Jeff', 18)
bark('Thomas', 15)
#print message saying we're done
print("Okay, We're all done")