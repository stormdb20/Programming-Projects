#empty dictionaries for movies
movies={}
movie={}
#add movie to movie dictionary and add other attributes
movie['name']='Forbidden Planet'
movie['year']=1957
movie['rating']='*****'
#replace movie year
movie['year']=1956
#assign the movie dictionary to the forbidden planet key
movies['Forbidden Planet']=movie
#dictionary with attributes of movie in full syntax
movie2={'name': 'I Was a Teenage Wolf', 'year': 1957, 'rating':'****'}
#change the rating attribute of movie2
movie2['rating']='***'
#add movie2 to movies dictionary using its name from the dictionary as the key
movies[movie2['name']]=movie2
#add movie to the movies dictionary without setting up another dictionary first
movies['Viking Women and The Sea Serpent']={'name':'Viking Women and The Sea Serpent', 'year': 1957, 'rating': '**'}
#another format for adding things to dictionaries in full syntax
movies['Vertigo']={'name': 'Vertigo',
                   'year': 1958,
                   'rating': '*****'}
#iterate through the names keys in the movies dictionary 
for name in movies:
    #assign the value in the name key of the movies dictionary to the movie dictionary 
    movie=movies[name]
    #look for four star or higher movies using length to comapare
    if len(movie['rating']) >= 4:
        print(movie['name'], movie['year'], movie['rating'])

