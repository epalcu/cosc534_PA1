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
            d_list.append(line)
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
        #print "1: " + word + " + " + item + " ---> {0}\n".format(password)
        if (test_password(password)):
            print "Password: {0}".format(password)
            return password
        else:
            password = item + word
            #print "2: " + item + " + " + word + " ---> {0}\n".format(password)
            if (test_password(password)):
                print "Password: {0}".format(password)
                return password
    return False

def kill_process(r):
    if r != 0:
        print "Killing process {0}.".format(r)
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
    process_results = Pool(4).map(create_password, words)

    results = comm.gather(list(process_results), root=0)
    kill_process(rank)

    for result in results:
        print set(result)
