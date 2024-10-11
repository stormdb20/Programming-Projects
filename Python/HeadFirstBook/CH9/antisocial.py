#Empty dictionary to add users to
users={}
#Add users to dictionary using name as a key and their info as another diction for the value
users['kim']={'email': 'kim@oreily.com', 'gender': 'F', 'age': 27, 'friends':['john', 'josh']}
users['john']={'email': 'john@abc.com', 'gender': 'M', 'age': 24, 'friends': ['kim','josh']}
users['josh']={'email': 'josh@wickedlysmart.com', 'gender': 'M', 'age': 32, 'friends': ['kim']}

max=1000
for name in users:
    user=users[name]
    friends=user['friends']
    if len(friends) < max:
        most_anti_social=name
        max=len(friends)
print('The most_anti_social frind is', most_anti_social)
