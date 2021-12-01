#!/usr/bin/python3
"""tracking the iss using
   api.open-notify.org/iss-now.json | Alta3 Research"""

# notice we no longer need to import urllib.request or json
import requests

## Define URL
ISSLocation = 'http://api.open-notify.org/iss-now.json'

def main():
    """runtime code"""

    ## Call the webservice
    ISSCheck = requests.get(ISSLocation)
    # send a post with requests.post()
    # send a put with requests.put()
    # send a delete with requests.delete()
    # send a head with requests.head()


    ## strip the json off the 200 that was returned by our API
    ## translate the json into python lists and dictionaries
    ISSLoc = ISSCheck.json()


    ## display our Pythonic data
    #print("\n\nConverted Python data")
    #print(ISSLoc)
    print('\n\nCURRENT LOCATION OF THE ISS:')
    #print('\n\nTimestamp:' + ISSLoc["timestamp"])
    print('\n\nLongitude:' + ISSLoc["iss_position"]["longitude"])
    print('\n\nLatitude:' + ISSLoc["iss_position"]["latitude"])
    #people = helmetson['people']
    #print(people)

if __name__ == "__main__":
    main()
