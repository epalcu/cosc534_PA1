import os
import sys
import hashlib
import base64
import time
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

# Read in dictionary into a list
def open_dictionary():
    d_list = []
    with open(sys.argv[1]) as fname:
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

def test_password(password_list):
    hashString = "DwYJS3xITeUb/TlJ/9vjdJSYRxdGuaR9BzqMadaivlI="
    for passwords in password_list:
        for password in passwords:
            string = "codingSeahorses:-1006154492:" + str(password)
            h = hashlib.sha256(string).digest()
            newString = base64.b64encode(h)
            if (newString == hashString):
                sys.stderr.write(password)
                open("password.txt", "w").write("Password: " + password)
                return True
    return False

def three_word_password(word):
    completed_words = open_completed()
    if word in completed_words:
        return False
    else:
        dict = open_dictionary()
        two_combos = [[''.join(word + item), ''.join(item + word), ''.join(word + ':' + item), ''.join(item + ':' + word)] for item in dictionary]
        combos = [[[''.join(two_combos[i][0] + dict[j]), ''.join(dict[i] + two_combos[i][0]),
                   ''.join(two_combos[i][1] + dict[j]), ''.join(dict[i] + two_combos[i][1]),
                   ''.join(two_combos[i][2].replace(':',  dict[j])),
                   ''.join(two_combos[i][3].replace(':',  dict[j]))]
                   for i in range(0, len(two_combos))] for j in range(0, len(dict))]
        passwords = map(test_password, combos)
        open("completed_words.txt", "a").write(word + '\n')
        if True in passwords:
            return True
        else:
            return False


if __name__ == "__main__":
    dictionary = open_dictionary()
    start = time.time()
    process_results = Pool().map(three_word_password, dictionary)
    end = time.time() - start
    print "Total elapsed computation time: {0} secs.".format(round(end, 2))
