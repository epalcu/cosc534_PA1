

#
# How To Run - Command Line Arguments:
# python3 ec_part5.py cracklib_ultrasmall
#


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

def test_password(word):
  completed_words = open_completed()
  if word in completed_words:
    return False
  else:
      chars = ['!','?','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}',';',':','.','/','<','>']
      number = ['0','1','2','3','4','5','6','7','8','9']
      numbers = ['12','13','11','69','06','22','21','23','14','10']
      wordsnum = []
      #  !@#$%^&*()-_=+[]{};’:”,./<>?  --- common: !  ---at beginning or end of word
      # numbers -- 1 is most common, 2, ect
              # -- 2 numbers : 12 13 11 69 06 22 21 23 14 10
      # upper lower -- first letter upper most common
      # https://csgillespie.wordpress.com/2011/06/16/character-occurrence-in-passwords/
      # 3 of the 4
      #assuming that only one letter will be changed to a number so either h3llo or hell0 or h4s


      ########################################################################
      #
      #  Create all formations with statistically common pre- and appensions.
      #
      ########################################################################

      word = word.lower()
      wordsnum.append(word)

      # Obtain forms of the word with symbols appended and prepended.
      for i in range(len(chars)):
        wordsnum.append(chars[i] + word)
        wordsnum.append(word + chars[i])

      # Obtain forms of the word with numbers appended and prepended.
      for i in range(len(number)):
        wordsnum.append(number[i] + word)
        wordsnum.append(word + number[i])

      # Obtain forms of the word with common double-digit #'s appended and prepended.
      for i in range(len(numbers)):
        wordsnum.append(numbers[i] + word)
        wordsnum.append(word + numbers[i])

      # Obtain permutations of common forms of replacing letters with numbers and symbols
      for w in wordsnum:
        for i in range(len(w)): #populate wordsnum list
          if w[i] == 'a':
            nword = list(w)
            nword[i] = '4'
            if "".join(nword) not in wordsnum:
              wordsnum.append("".join(nword))
            nword = list(w)
            nword[i] = '@'
            if "".join(nword) not in wordsnum:
              wordsnum.append("".join(nword))
          if w[i] == 'o':
            nword = list(w)
            nword[i] = '0'
            if "".join(nword) not in wordsnum:
              wordsnum.append("".join(nword))
          if w[i] == 'e':
            nword = list(w)
            nword[i] = '3'
            if "".join(nword) not in wordsnum:
              wordsnum.append("".join(nword))
          if w[i] == 'b':
            nword = list(w)
            nword[i] = '6'
            if "".join(nword) not in wordsnum:
              wordsnum.append("".join(nword))
          if w[i] == 's':
            nword = list(w)
            nword[i] = '5'
            if "".join(nword) not in wordsnum:
              wordsnum.append("".join(nword))
            nword = list(w)
            nword[i] = '$'
            if "".join(nword) not in wordsnum:
              wordsnum.append("".join(nword))
          # Permute upper case as well.
          if ord(w[i]) >= 97 and ord(w[i]) <= 122:
            nword = list(w)
            nword[i] = chr(ord(nword[i]) - 32)
            if "".join(nword) not in wordsnum:
              wordsnum.append("".join(nword))

      # Test if any of the permutations were the password
      for w in wordsnum:
        print(w)
        w = w.encode('utf-8')
        h = hashlib.sha256(w).digest()
        newString = base64.b64encode(h)

        if(newString == "DwYJS3xITeUb/TlJ/9vjdJSYRxdGuaR9BzqMadaivlI="):
          open("password.txt", "w").write("Password: " + w)
          sys.exit(0)
        open("completed_words.txt", "a").write(word + '\n')

if __name__ == "__main__":
  dictionary = open_dictionary(sys.argv[1])
  open("completed_words.txt", "w").write('\n')
    
  Pool(4).map(test_password, dictionary)

          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
            
            
            
            
            
