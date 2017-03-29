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
    dictionary = open_dictionary(dictionary)
    first_combo = [''.join(map(str, word) + map(str, ":" + item)) for item in dictionary]
    second_combo = [''.join(map(str, item) + map(str, ":" + word)) for item in dictionary]
    password = test_password([first_combo, second_combo])
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
