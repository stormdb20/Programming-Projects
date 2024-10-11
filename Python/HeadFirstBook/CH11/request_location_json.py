#import json and requests modules on same line
import json, requests
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