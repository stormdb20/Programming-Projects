#import the request module
import requests
#var to hold url of web api to be requested
url="http://api.open-notify.org/iss-now.json"
#var to hold request get function that will be passed the url
response= requests.get(url)
#compare to check if the status code is 200 which is request fulfilled without errors
if (response.status_code == 200):
    print('Good to go', response.text)
    
else:
    print("Trouble O Trouble", response.status_code)