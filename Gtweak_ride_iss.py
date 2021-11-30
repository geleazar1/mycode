#!/usr/bin/python3
"""Alta3 Research - tracking ISS updated output"""

import urllib.request
import json

MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    """reading json from api"""
    # call the api
    groundctrl = urllib.request.urlopen(MAJORTOM)

    # strip off the attachment (JSON) and read it
    # the problem here, is that it will read out as a string
    helmet = groundctrl.read()


    helmetson = json.loads(helmet.decode("utf-8"))

    # append names into the list
    newhelmet = helmetson.append({"name" : "Eddie Kopra"}, {"name" : "James Peake"}, {"name" : "Yurie Kopra"}, {"name" : "Buzz Aldrin"})
    # display people in space
    print("People in space: " + str(helmetson["number"]))

    # display every item in a list
    for astro in newhelmet["people"]:
        # display ONLY the name value associated with astro
        print(astro["name"] + " on the " + astro["craft"])

if __name__ == "__main__":
    main()

