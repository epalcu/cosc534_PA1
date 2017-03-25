import os
import sys
import hashlib
import base64
from multiprocessing import Pool

# Read in dictionary into a list
def open_dictionary(d_list):
    with open("cracklib-small") as fname:
        lines = fname.readlines()
        for line in lines:
            d_list.append(line[:-1])
    fname.close()
    return d_list

def test_password(password):
    challengeString = "202555186"
    userName = "codingSeahorses"
    hashString = "XfqX+EDWLYKgOmM67+G+lOGf/Dmb9WfchMrquw5xpE0="
    string = userName + ":" + challengeString + ":" + password
    h = hashlib.sha256(string).digest()
    newString = base64.b64encode(h)
    if (newString == hashString):
        return True
    else:
        return False

def create_password(word):
    dictionary = []
    dictionary = open_dictionary(dictionary)
    for item in dictionary:
        password = word + item
        if (test_password(password)):
            print "Password: {0}".format(password)
            exit(0)
        else:
            password = item + word
            if (test_password(password)):
                print "Password: {0}".format(password)
                exit(0)

if __name__ == "__main__":
    dictionary = []
    dictionary = open_dictionary(dictionary)

    Pool().map(create_password, dictionary)
