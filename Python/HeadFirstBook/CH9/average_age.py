#Emoty dictionary to add users to
users={}
#Add users to dictionary using name as a key and their info as another diction for the value
users['kim']={'email': 'kim@oreily.com', 'gender': 'F', 'age': 27, 'friends':['john', 'josh']}
users['john']={'email': 'john@abc.com', 'gender': 'M', 'age': 24, 'friends': ['kim','josh']}
users['josh']={'email': 'josh@wickedlysmart.com', 'gender': 'M', 'age': 32, 'friends': ['kim']}

#function to compute average age of friends passing a string as an argument
def average_age(username):
    #use global users dictionary within the function
    global users
    #var to get users attributes dictionary EX. users would be kim going by the first function call at the bottom
    user=users[username]
    #var to hold friends list EX. in this case kims friends
    friends=user['friends']
    #var to hold sum count
    sum=0
    #iterate through friends list names is just another form of saying string that works for this code scenario
    for name in friends:
        #assigning the current string name to var string
        friend=users[name]
        #updating the sum var by adding the current friends age
        sum=sum+friend['age']
    #var use the current value in sum var divided by length of friends list of current username to get avg age    
    average=sum/len(friends)
    #print current users that was passed to function with message and value of the average
    print(username, 's friends have an average age of', average)

average_age('kim')
average_age('john')
average_age('josh')

        