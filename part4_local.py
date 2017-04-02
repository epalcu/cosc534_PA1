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

def three_word_password(word):
    completed_words = open_completed()
    if word in completed_words:
        return False
    else:
        dict = open_dictionary(sys.argv[2])
        for item1 in range(0, len(dict)):
            for item2 in range(0, len(dict)):
                # Test combination one
                string = "codingSeahorses:-1006154492:" + word + dict[item1] + dict[item2]
                h = hashlib.sha256(string).digest()
                newString = base64.b64encode(h)
                if (newString == "DwYJS3xITeUb/TlJ/9vjdJSYRxdGuaR9BzqMadaivlI="):
                    sys.stderr.write(word + dict[item1] + dict[item2])
                    open("password.txt", "w").write("Password: " + word + dict[item1] + dict[item2])
                    return word + dict[item1] + dict[item2]
                # Test combination two
                string = "codingSeahorses:-1006154492:" + word + dict[item2] + dict[item1]
                h = hashlib.sha256(string).digest()
                newString = base64.b64encode(h)
                if (newString == "DwYJS3xITeUb/TlJ/9vjdJSYRxdGuaR9BzqMadaivlI="):
                    sys.stderr.write(word + dict[item2] + dict[item1])
                    open("password.txt", "w").write("Password: " + word + dict[item2] + dict[item1])
                    return word + dict[item2] + dict[item1]
                # Test combination three
                string = "codingSeahorses:-1006154492:" + dict[item1] + word + dict[item2]
                h = hashlib.sha256(string).digest()
                newString = base64.b64encode(h)
                if (newString == "DwYJS3xITeUb/TlJ/9vjdJSYRxdGuaR9BzqMadaivlI="):
                    sys.stderr.write(dict[item1] + word + dict[item2])
                    open("password.txt", "w").write("Password: " + dict[item1] + word + dict[item2])
                    return dict[item1] + word + dict[item2]
                # Test combination four
                string = "codingSeahorses:-1006154492:" + dict[item1] + dict[item2] + word
                h = hashlib.sha256(string).digest()
                newString = base64.b64encode(h)
                if (newString == "DwYJS3xITeUb/TlJ/9vjdJSYRxdGuaR9BzqMadaivlI="):
                    sys.stderr.write(dict[item1] + dict[item2] + word)
                    open("password.txt", "w").write("Password: " + dict[item1] + dict[item2] + word)
                    return dict[item1] + dict[item2] + word
                # Test combination five
                string = "codingSeahorses:-1006154492:" + dict[item2] + word + dict[item1]
                h = hashlib.sha256(string).digest()
                newString = base64.b64encode(h)
                if (newString == "DwYJS3xITeUb/TlJ/9vjdJSYRxdGuaR9BzqMadaivlI="):
                    sys.stderr.write(dict[item2] + word + dict[item1])
                    open("password.txt", "w").write("Password: " + dict[item2] + word + dict[item1])
                    return dict[item2] + word + dict[item1]
                # Test combination six
                string = "codingSeahorses:-1006154492:" + dict[item2] + dict[item1] + word
                h = hashlib.sha256(string).digest()
                newString = base64.b64encode(h)
                if (newString == "DwYJS3xITeUb/TlJ/9vjdJSYRxdGuaR9BzqMadaivlI="):
                    sys.stderr.write(dict[item2] + dict[item1] + word)
                    open("password.txt", "w").write("Password: " + dict[item2] + dict[item1] + word)
                    return dict[item2] + dict[item1] + word
        #print "Completed word: {0}".format(word)
        open("completed_words.txt", "a").write(word + '\n')


if __name__ == "__main__":
    dictionary = open_dictionary(sys.argv[1])
    #start = time.time()
    Pool(4).map(three_word_password, dictionary)
    #end = time.time() - start
    #print "Total elapsed computation time: {0} secs.".format(round(end, 2))
