#import json, turtle, and requests modules on same line
import json, requests, turtle
#function to move the turtle to the long and lat
def move_iss(long, lat):
    global iss
    iss.penup()
    iss.goto(long, lat)
    iss.pendown()


#Var for creating screen and then setting attributes for the screen
screen=turtle.Screen()
screen.setup(1000,500)
screen.bgpic('earth.gif')
screen.setworldcoordinates(-180,-90,180,90)

#Instantiate turtle and register gif as a shape then change the turtle's shape to the gif file
iss=turtle.Turtle()
turtle.register_shape("iss.gif")
iss.shape("iss.gif")

#var to hold url of web api to be requested
url="http://api.open-notify.org/iss-now.json"
#var to hold request get function that will be passed the url
response= requests.get(url)
#compare to check if the status code is 200 which is request fulfilled without errors
if (response.status_code == 200):
    #var to hold the json.loads converts response text to string and then a python dictionary
    response_dictionary= json.loads(response.text)
    #var to hold iss position from response dicitonary which holds the response text created from json loads then print location
    position= response_dictionary['iss_position']
    print('International Space Station at ' +
        position['latitude'] + ', ' + position['longitude'])   
#print message and the response status code that did not equal 200  
else:
    print("Trouble O Trouble", response.status_code)
    
turtle.mainloop()