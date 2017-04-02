import os
import sys
import hashlib
import base64
import time
from multiprocessing import Pool

# Read in dictionary into a list
def open_dictionary(dict):
    d_list = []
    with open(dict) as fname:
        lines = fname.readlines()
        for line in lines:
            d_list.append(line[:-1])
    fname.close()
    return d_list

def open_completed():
    c_list = []
    with open("completed_words.txt") as fname:
        lines = fname.readlines()
        for line in lines:
            c_list.append(line[:-1])
    fname.close()
    return c_list

def test_password(password):
    #print "Testing password: {0}".format(password)
    string = "codingSeahorses:-1006154492:" + str(password)
    h = hashlib.sha256(string).digest()
    newString = base64.b64encode(h)
    if (newString == "DwYJS3xITeUb/TlJ/9vjdJSYRxdGuaR9BzqMadaivlI="):
        sys.stderr.write(password)
        open("password.txt", "w").write("Password: " + password)
        return True
    else:
        return False

def three_word_password(word):
    completed_words = open_completed()
    if word in completed_words:
        return False
    else:
        passwords = []
        dict = open_dictionary(sys.argv[2])
        for item1 in range(0, len(dict)):
            print item1
            for item2 in range(0, len(dict)):
                passwords.append(word + dict[item1] + dict[item2])
                passwords.append(word + dict[item2] + dict[item1])
                passwords.append(dict[item1] + word + dict[item2])
                passwords.append(dict[item1] + dict[item2] + word)
                passwords.append(dict[item2] + word + dict[item1])
                passwords.append(dict[item2] + dict[item1] + word)
                passwords = map(test_password, passwords)
                passwords[:] = []
        print "Completed word: {0}".format(word)
        open("completed_words.txt", "a").write(word + '\n')


if __name__ == "__main__":
    dictionary = open_dictionary(sys.argv[1])
    start = time.time()
    Pool(4).map(three_word_password, dictionary)
    end = time.time() - start
    print "Total elapsed computation time: {0} secs.".format(round(end, 2))
