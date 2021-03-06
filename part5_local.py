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

def test_password(passwords):
    hashString = "ppzJy3VakbXRWLzj7udaNny5iZ4wSMsoiuegQLoWyrI="
    for password in passwords:
        string = "codingSeahorses:1362111551:" + password
        h = hashlib.sha256(string).digest()
        newString = base64.b64encode(h)
        if (newString == hashString):
            sys.stderr.write(password)
            return True, password
    return False, None

def three_word_password(word):
    dictionary = []
    passwords = []
    dictionary = open_dictionary(dictionary)
    for item1 in dictionary:
        for item2 in dictionary:
            passwords.append(word + item1 + item2)
            passwords.append(word + item2 + item1)
            passwords.append(item1 + word + item2)
            passwords.append(item1 + item2 + word)
            passwords.append(item2 + word + item1)
            passwords.append(item2 + item1 + word)
            password = test_password(passwords)
            if (password[0] == True):
                return password[1]
    return False

if __name__ == "__main__":
    dictionary = []
    dictionary = open_dictionary(dictionary)
    process_results = Pool(32).map(three_word_password, dictionary)

    for result in process_results:
        print set(result)
