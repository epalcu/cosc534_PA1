import os
import sys
import hashlib
import base64
from mpi4py import MPI

# Read in dictionary into a list
def open_dictionary(d_list):
    with open("cracklib-small") as fname:
        lines = fname.readlines()
        for line in lines:
            d_list.append(line[:-1])
    fname.close()
    return d_list

def test_password(password):
    string = "codingSeahorses:-1128626187:" + password
    h = hashlib.sha256(string).digest()
    newString = base64.b64encode(h)
    if (newString == hashString):
        return True
    else:
        return False

def create_password(words):
    dictionary = []
    dictionary = open_dictionary(dictionary)
    for word in words:
        for item in dictionary:
            password = word + item
            if (test_password(password)):
                print "Password: {0}".format(password)
                exit(0)
            else:
                password = item + word
                if (test_password(password)):
                    print "Password: {0}".format(password)
                    exit(0)

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
    create_password(words)
