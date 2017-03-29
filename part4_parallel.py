import os
import sys
import hashlib
import base64
from mpi4py import MPI
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
    hashString = "DwYJS3xITeUb/TlJ/9vjdJSYRxdGuaR9BzqMadaivlI="
    for password in passwords:
        string = "codingSeahorses:-1006154492:" + str(password)
        h = hashlib.sha256(string).digest()
        newString = base64.b64encode(h)
        if (newString == hashString):
            sys.stderr.write(password)
            return True, password
    return False, None

def three_word_password(word):
    dictionary = []
    dict = open_dictionary(dictionary)
    two_combos = [[''.join(word + item), ''.join(item + word), ''.join(word + ':' + item), ''.join(item + ':' + word)] for item in dictionary]
    combos = [[''.join(two_combos[i][0] + dict[i]), ''.join(dict[i] + two_combos[i][0]),
               ''.join(two_combos[i][1] + dict[i]), ''.join(dict[i] + two_combos[i][1]),
               ''.join(two_combos[i][2].replace(':',  dict[i])),
               ''.join(two_combos[i][3].replace(':',  dict[i]))] for i in range(0, len(two_combos))]
    password = map(test_password, combos)
    if (password[0] == True):
        return password[1]
    else:
        return False
def kill_process(r):
    if r != 0:
        #print "Killing process {0}.".format(r)
        sys.exit(0)

if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    if (rank == 0):
        dictionary = []
        dictionary = open_dictionary(dictionary)
        slices = [[] for i in range(size)]
        for i, slice in enumerate(dictionary):
            slices[i % size].append(slice)
    else:
        dictionary = None
        slices = None

    words = comm.scatter(slices, root=0)
    process_results = Pool(4).map(three_word_password, words)

    results = comm.gather(list(process_results), root=0)
    kill_process(rank)

    for result in results:
        print set(result)
