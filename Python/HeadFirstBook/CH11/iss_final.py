#import json, turtle, and requests modules on same line
import json, requests, turtle
#var to instantiate turtle
iss=turtle.Turtle()
#function to move the turtle to the long and lat
def move_iss(long, lat):
    global iss
    iss.penup()
    iss.goto(long, lat)
    iss.pendown()

#Var for creating screen and then setting attributes for the screen
def setup(window):
    '''Function to make the screen for the turtle, change
    the background to the earth map, set the world coordinates, register
    the turtle shape as the iss gif file, and change it's shape ti the iss gif file.'''
    global iss
    screen=turtle.Screen()
    window.setup(1000,500)
    window.bgpic('earth.gif')
    window.setworldcoordinates(-180,-90,180,90)
#Instantiate turtle and register gif as a shape then change the turtle's shape to the gif file
    turtle.register_shape("iss.gif")
    iss.shape("iss.gif")

def track_iss():
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
        long=float(position['longitude'])
        lat=float(position['latitude'])
        move_iss(lat,long)
#print message and the response status code that did not equal 200  
    else:
        print("Trouble O Trouble", response.status_code)
    #Guessing it means create a widget and pass it a time and action to be taken after that amount of time
    widget=turtle.getcanvas()
    widget.after(5000, track_iss)
def main():
    global iss 
    screen= turtle.Screen()
    setup(screen)
    track_iss()
    
if __name__ == "__main__":
    main()
    turtle.mainloop()
    
    