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
    
    chars = ['!','?','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}',';',':','.','/','<'.'>']
    number = ['1','2','3','4','5','6','7','8','9']
    numbers = ['12','13','11','69','06','22','21','23','14','10']
    wordsnum = []
    #  !@#$%^&*()-_=+[]{};’:”,./<>?  --- common: !  ---at beginning or end of word
    # numbers -- 1 is most common, 2, ect
            # -- 2 numbers : 12 13 11 69 06 22 21 23 14 10
    # upper lower -- first letter upper most common
    # https://csgillespie.wordpress.com/2011/06/16/character-occurrence-in-passwords/
    # 3 of the 4
    #assuming that only one letter will be changed to a number so either h3llo or hell0 or h4s



    word = word.upper()
  
    for(i in range(len(chars))):
      #original word
      chars[i] + word  #put a chars at the beginning

      word + chars[i] #put the chars at the end of the word
      
      #upper word

      #number words

    for(j in range(len(number))):
      
      for(i in range(len word): #populate wordsnum list
        word.lower();
        if word[i] == 'a':
          nword = word
          nword[i] = '4'
          wordsnum.append(nword[i])
        if word [i] == 'o':
          nword = word
          nword[i] = '0'
          wordsnum.append(nword[i])
        if word [i] == 'e':
          nword = word
          nword[i] = '3'
          wordsnum.append(nword[i])
        if word [i] == 'b':
          nword = word
          nword[i] = '6'
          wordsnum.append(nword[i])
        if word [i] == 's':
          nword = word
          nword[i] = '5'
          wordsnum.append(nword[i])
        
          
      number[j] + word

      word + number[j]

    for(k in range(len(numbers))):
      
      numbers[k] + word

      word + number[k]

    completed_words = open_completed()
    if word in completed_words:
      return False
      else:
      dict = open_dictionary(sys.argv[2])
      for item1 in range(0, len(dict)):
        for item2 in range(0, len(dict)):
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
