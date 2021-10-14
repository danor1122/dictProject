from isExist import is_exist, write_in_file
import string
import linecache
# from string import find,join


path = '/home/acrooxy/Desktop/dictProject/project1/dict.txt'

def findfn():
    is_exist()
    f = open(path, 'r')

    for line in f:
        wordlist = [line.split(' ', 2)[1] for line in f]
        
        find_it = str(input("Which word would you like to fine? : "))
        if find_it in wordlist:
            print("Word has been found!\n")
            a = wordlist.index(find_it) + 2
            
            poem =  linecache.getline('dict.txt', a) # printing exact poem
            print("Poem:",poem)     
            
        else:
            print("Could not find this word in Dictionary.\n")
# findfn()