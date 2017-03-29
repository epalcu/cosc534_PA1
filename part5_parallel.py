import os
import sys
import hashlib
import base64
from mpi4py import MPI
from multiprocessing import Pool

# Read in dictionary into a list
def open_dictionary(d_list):
    with open("cracklib-smaller.txt") as fname:
        lines = fname.readlines()
        for line in lines:
            d_list.append(line[:-1])
    fname.close()
    return d_list

def test_password(passwords):
    challengeString = "1362111551"
    userName = "codingSeahorses"
    hashString = "ppzJy3VakbXRWLzj7udaNny5iZ4wSMsoiuegQLoWyrI="
    for password in passwords:
        string = userName + ":" + challengeString + ":" + password
        h = hashlib.sha256(string).digest()
        newString = base64.b64encode(h)
        if (newString == hashString):
            sys.stderr.write(password)
            return True, password
    print "Password not found..\n"
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
            value, password = test_password(passwords)
            if (value == True):
                return password
    print "Moving on to next word in processes test set..\n"
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
