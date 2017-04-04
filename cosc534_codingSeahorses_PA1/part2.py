import os
import sys
import hashlib
import base64

challengeString = "-1128626187"
userName = "codingSeahorses"
hashString = "1FnK0Fv7JOHZgh82rtmWZDW9Y9KQdgz9Gh6E6Cs35AY="
hashSecret = "R5SOwt7UwrKo0sBXxDhSNXeCpa7Dffl0pHHG0bHIrUY="
dictionary = []

# Read in dictionary into a list
def open_dictionary(d_list, file):
    with open(file) as fname:
        lines = fname.readlines()
        for line in lines:
            d_list.append(line[:-1])
    fname.close()
    return d_list


if __name__ == "__main__":
    dictionary = []
    dictionary = open_dictionary(dictionary, sys.argv[1])

    # Cycle through each dictionary word until the hash of the concatenated string
    # is equal to the initally received hashString
    for i in dictionary:
        string = userName + ":" + challengeString + ":" + i
        h = hashlib.sha256(string).digest()
        newString = base64.b64encode(h)
        if (newString == hashString):
            print "Password: {0}".format(i)
            break
