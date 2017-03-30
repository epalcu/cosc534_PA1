import os
import sys
import hashlib
import base64
import time
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

# Read in dictionary into a list
def open_dictionary(d_list):
    with open("cracklib-smallest.txt") as fname:
        lines = fname.readlines()
        for line in lines:
            d_list.append(line[:-1])
    fname.close()
    return d_list

def test_password(password):
    hashString = "DwYJS3xITeUb/TlJ/9vjdJSYRxdGuaR9BzqMadaivlI="
    string = "codingSeahorses:-1006154492:" + password
    h = hashlib.sha256(string).digest()
    newString = base64.b64encode(h)
    if (newString == hashString):
        sys.stderr.write(password)
        return True
    else:
        return False

def traverse_passwords(passwords):
    return map(test_password, passwords)

def traverse_combos(combos):
    return map(traverse_passwords, combos)

def three_word_password(word):
    dictionary = []
    dict = open_dictionary(dictionary)
    two_combos = [[''.join(word + item), ''.join(item + word), ''.join(word + ':' + item), ''.join(item + ':' + word)] for item in dictionary]
    combos = [[[''.join(two_combos[i][0] + dict[j]), ''.join(dict[i] + two_combos[i][0]),
               ''.join(two_combos[i][1] + dict[j]), ''.join(dict[i] + two_combos[i][1]),
               ''.join(two_combos[i][2].replace(':',  dict[j])),
               ''.join(two_combos[i][3].replace(':',  dict[j]))]
               for i in range(0, len(two_combos))] for j in range(0, len(dict))]
    passwords = ThreadPool(8).map(traverse_combos, combos)
    if True in passwords:
        return True
    else:
        sys.stderr.write("Password not found.\n")
        return False


if __name__ == "__main__":
    dictionary = []
    dictionary = open_dictionary(dictionary)
    start = time.time()
    process_results = Pool(16).map(three_word_password, dictionary)
    end = time.time() - start
    print "Total elapsed computation time: {0} secs.".format(round(end, 2))
