from isExist import is_exist, write_in_file
import string
# from string import find,join

path = '/home/acrooxy/Desktop/dictProject/project1/dict.txt'

def findfn():
    is_exist()
    f = open(path, 'r')

    for line in f:
        wordlist = [line.split(' ', 2)[1] for line in f]
        print(wordlist)
        find_it = str(input("Which word would you like to fine? : "))
        if find_it in wordlist:
            print("Word has been found!")
        else:
            print("Could not find this word in Dictionary.")

    # f.close()
    # text = join(list, "")
    # find_it = find(text, "im")
    # if find_it > 1:
    #     print("word has been found.")
    # else:
    #     print("Could'nt find this word.")
    # if "yes" in list:
    #     print('founded')
    # else:
    #     print("at least program is working")
