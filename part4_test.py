import os
import sys
import hashlib
import base64
import time
from multiprocessing import Pool

# Read in dictionary into a list
def open_dictionary(d_list):
    with open("cracklib-smallest.txt") as fname:
        lines = fname.readlines()
        for line in lines:
            d_list.append(line[:-1])
    fname.close()
    return d_list

def test_password(password_list):
    hashString = "DwYJS3xITeUb/TlJ/9vjdJSYRxdGuaR9BzqMadaivlI="
    for password in password_list:
        string = "codingSeahorses:-1006154492:" + password
        h = hashlib.sha256(string).digest()
        newString = base64.b64encode(h)
        if (newString == hashString):
            sys.stderr.write(password)
            return True
    return False

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
            password = map(test_password, passwords)
            if True in password:
                return True
    sys.stderr.write("Password not found.\n")
    return False


if __name__ == "__main__":
    dictionary = []
    dictionary = open_dictionary(dictionary)
    start = time.time()
    process_results = Pool(32).map(three_word_password, dictionary)
    end = time.time() - start
    print "Total elapsed computation time: {0} secs.".format(round(end, 2))
